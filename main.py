import subprocess
from datetime import datetime

PLAYLISTS = "./playlists.txt"


def print_to_console(value: str):
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S: ") + value)


def parse_playlists() -> list:
    content = open(PLAYLISTS,'r',encoding="utf-8")
    playlists = []
    for line in content:
        data = line.split(",")
        playlists.append((data[0].strip(),data[1].strip()))
    return playlists
        

def parse_tracks(playlist: str) -> list:
    content = open(playlist,'r',encoding="utf-8")
    tracks = []
    for line in content:
        if line[0] == "#": continue
        line = line.strip().replace('"','')
        data = line.split("/")
        tracks.append((line,data.pop().replace("'","\'")))
    return tracks


def make_symlink(track: list, destination: str):
    source = track[0]
    link = f"{destination}{track[1]}"
    try:
        result = subprocess.run(f'ln -sf "{source}" "{link}"', shell=True, check=True)
        print_to_console(f"Created symlink:\n    {result}")
    except Exception as e:
        print_to_console(f"Error creating symlink:\n    {e}")


def main():
    playlists = parse_playlists()
    for playlist in playlists:
        tracks = parse_tracks(playlist[0])
        destination = playlist[1]
        for track in tracks:
            make_symlink(track,destination)


if __name__ == "__main__":
    print_to_console("Starting Script")
    main()
    print_to_console("Script Completed")
