from modules.file_organizer import FileOrganizer
from modules.web_scraper import WebScraper
from modules.system_monitor import SystemMonitor
from config.settings import *

def main():

    print("Automation Suite Started\n")

    organizer = FileOrganizer(WATCH_FOLDER, ORGANIZED_FOLDER)
    organizer.organize()

    scraper = WebScraper(SCRAPE_URL)
    scraper.scrape_quotes()

    monitor = SystemMonitor()
    monitor.check_system()


if __name__ == "__main__":
    main()