"""Local package checks and private evidence folder, Python 3.10+; no network."""
import argparse
import datetime as dt
import hashlib
import json
from pathlib import Path
import shutil
import zipfile

ROOT = Path(__file__).resolve().parent
SLOTS = ('A1', 'B1', 'A2', 'B2', 'A3', 'B3')


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read(path):
    return json.loads(path.read_text(encoding='utf-8-sig'))


def save(path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def verify():
    manifest = read(ROOT / 'herkunft/paket.json')
    for item in manifest['files']:
        path = ROOT / item['path']
        if not path.is_file() or sha(path) != item['sha256']:
            raise ValueError('Paketdatei fehlt/verändert: ' + item['path'])
    expected = {'ledger.py', 'ledger_test.py', 'instructions.md', 'aufgabenvertrag.md'}
    if {p.name for p in (ROOT / 'eingabe').iterdir()} != expected:
        raise ValueError('Eingabeordner enthält unerwartete Dateien')
    print('Paket-Hashes und vier Eingabedateien geprüft.')


def initialize(dest):
    verify()
    if dest.resolve().is_relative_to(ROOT.resolve()):
        raise ValueError('Nachweise außerhalb des gesamten Hilfs-Repositories speichern.')
    dest.mkdir(parents=True, exist_ok=False)
    for p in (ROOT / 'vorlagen').iterdir():
        if p.is_file():
            shutil.copyfile(p, dest / p.name)
    (dest / 'vorab').mkdir()
    shutil.copyfile(ROOT / 'herkunft/paket.json', dest / 'vorab/paket.json')
    for slot in SLOTS:
        target = dest / slot
        target.mkdir()
        template = read(ROOT / 'vorlagen/slot.json')
        template['slot'] = slot
        save(target / 'protokoll.json', template)
        shutil.copyfile(ROOT / 'anleitung/PRO-SLOT.md', target / 'LESEN.md')
    print('Lokale Nachweise angelegt:', dest)


def seal(dest):
    verify()
    target = dest / 'V-FIXIERT.json'
    if target.exists():
        raise ValueError('Stand V existiert bereits; nicht überschreiben.')
    state = read(dest / 'V-MAC.json')
    required = [k for k in state if not k.startswith('_')]
    missing = [k for k in required if state[k] in (None, '', [])]
    if missing:
        raise ValueError('Mac-Angaben fehlen: ' + ', '.join(missing))
    if state['mode'] != 'Ask' or state['plan'] != 'Business':
        raise ValueError('Ask/Business bestätigen; Abweichung vor A1 klären.')
    if state['preflight_complete'] is not True:
        raise ValueError('Vollständige Vorabprüfung fehlt.')
    if any(read(dest / s / 'protokoll.json').get('sent_at') for s in SLOTS):
        raise ValueError('Bereits gesendeter Slot; keine nachträgliche Vorabfixierung.')
    paths = sorted(p for p in (dest / 'vorab').rglob('*') if p.is_file())
    if not paths or not any(p.name != 'paket.json' for p in paths):
        raise ValueError('Oberflächen-/Einstellungsnachweise unter vorab fehlen.')
    paths.append(dest / 'V-MAC.json')
    save(target, {'created_at': dt.datetime.now(dt.timezone.utc).isoformat(),
                  'package_manifest_sha256': sha(ROOT / 'herkunft/paket.json'),
                  'source_commit': read(ROOT / 'herkunft/paket.json')['source_commit'],
                  'files': [{'path': p.relative_to(dest).as_posix(), 'sha256': sha(p)} for p in paths],
                  'limit': 'Lokale Hashfixierung, keine unabhängige Zeitbeglaubigung. Vor A1 separat sichern.'})
    print('Stand V fixiert:', target)


def return_zip(dest):
    target = dest.with_name(dest.name + '-rueckgabe.zip')
    if target.exists():
        raise ValueError('Rückgabe-ZIP existiert bereits.')
    if not (dest / 'V-FIXIERT.json').exists():
        raise ValueError('Stand V fehlt.')
    files = [p for p in sorted(dest.rglob('*')) if p.is_file() and p.name != 'rueckgabe-hashes.json']
    save(dest / 'rueckgabe-hashes.json', [{'path': p.relative_to(dest).as_posix(), 'sha256': sha(p)} for p in files])
    with zipfile.ZipFile(target, 'x', compression=zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(dest.rglob('*')):
            if path.is_file():
                archive.write(path, path.relative_to(dest).as_posix())
    print('Privat an den PC übertragen:', target)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=['verify', 'init', 'seal', 'return'])
    parser.add_argument('folder', nargs='?', type=Path)
    args = parser.parse_args()
    if args.action == 'verify':
        verify()
    elif args.folder is None:
        parser.error('Nachweisordner erforderlich')
    elif args.action == 'init':
        initialize(args.folder)
    elif args.action == 'seal':
        seal(args.folder)
    else:
        return_zip(args.folder)


if __name__ == '__main__':
    main()
