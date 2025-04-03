from core.file_crawler import crawl_python_files
from core.git_pusher import commit_and_push

def sync_codebase():
    crawl_python_files()
    commit_and_push()

if __name__ == "__main__":
    sync_codebase()
