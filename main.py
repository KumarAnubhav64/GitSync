from pathlib import Path
from ftp_server.ftp_server import FTPServerApp
from custom_git.custom_git import CustomGit
import typer

app = typer.Typer()

@app.command()
def run_git(repo_path: str):
    """Run the Git system."""
    repo_path = Path(repo_path)
    git = CustomGit(repo_path)
    git.init()
    git.add()
    git.commit()
    

@app.command()
def run_ftp(shared_folder: str, host: str = "0.0.0.0", port: int = 2121):
    """Run the FTP server."""
    shared_folder = Path(shared_folder)
    ftp = FTPServerApp(shared_folder, host, port)
    ftp.setup_server()
    ftp.start()

@app.command()
def run_combined(repo_path: str, shared_folder: str, host: str = "127.0.0.1", port: int = 2121):
    """Run both the Git system and the FTP server."""
    # Start the Git system
    repo_path = Path(repo_path)
    git = CustomGit(repo_path)
    git.init()

    # Start the FTP serve r
    shared_folder = Path(shared_folder)
    ftp = FTPServerApp(shared_folder, host, port)
    ftp.setup_server()
    ftp.start()

if __name__ == "__main__":
    app()
