import sqlite3

# 連接到 SQLite 資料庫（如果不存在，將會自動創建）
conn = sqlite3.connect("companies.db")

# 創建游標
cursor = conn.cursor()

# 創建資料表
cursor.execute("""
CREATE TABLE IF NOT EXISTS companies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_name TEXT,
    founders TEXT,
    headquarters_country TEXT,
    headquarters_state TEXT,
    founded_year INTEGER,
    number_of_employees INTEGER,
    revenue_billion_usd REAL
)
""")

# 插入資料
cursor.executemany(
    """
INSERT INTO companies (company_name, founders, headquarters_country, headquarters_state, founded_year, number_of_employees, revenue_billion_usd)
VALUES (?, ?, ?, ?, ?, ?, ?)
""",
    [
        (
            "Apple Inc.",
            "Steve Jobs, Steve Wozniak, Ronald Wayne",
            "USA",
            "California",
            1976,
            164000,
            394.33,
        ),
        (
            "Microsoft Corp.",
            "Bill Gates, Paul Allen",
            "USA",
            "Washington",
            1975,
            221000,
            211.92,
        ),
        (
            "NVIDIA Corp.",
            "Jensen Huang, Chris Malachowsky, Curtis Priem",
            "USA",
            "California",
            1993,
            26700,
            26.91,
        ),
        (
            "Alphabet Inc.",
            "Larry Page, Sergey Brin",
            "USA",
            "California",
            1998,
            190234,
            257.64,
        ),
        ("Amazon.com Inc.", "Jeff Bezos", "USA", "Washington", 1994, 154800, 502.19),
        (
            "Meta Platforms Inc.",
            "Mark Zuckerberg, Eduardo Saverin, Andrew McCollum, Dustin Moskovitz, Chris Hughes",
            "USA",
            "California",
            2004,
            86532,
            116.61,
        ),
        (
            "Tesla Inc.",
            "Elon Musk, JB Straubel, Martin Eberhard, Marc Tarpenning",
            "USA",
            "California",
            2003,
            99290,
            81.46,
        ),
        (
            "Berkshire Hathaway",
            "Warren Buffett",
            "USA",
            "Nebraska",
            1839,
            360711,
            276.09,
        ),
        ("Taiwan Semiconductor", "Morris Chang", "Taiwan", "", 1987, 56800, 57.2),
        (
            "Saudi Aramco",
            "King Abdulaziz Al Saud",
            "Saudi Arabia",
            "",
            1933,
            66836,
            400.4,
        ),
        (
            "ExxonMobil",
            "John D. Rockefeller, Henry Flagler",
            "USA",
            "Texas",
            1999,
            63000,
            402.7,
        ),
        (
            "Johnson & Johnson",
            "Robert Wood Johnson I, James Wood Johnson",
            "USA",
            "New Jersey",
            1886,
            152700,
            93.77,
        ),
        (
            "JPMorgan Chase",
            "Aaron Burr, John Thompson",
            "USA",
            "New York",
            1799,
            271025,
            128.7,
        ),
        ("Visa Inc.", "Dee Hock", "USA", "California", 1958, 21000, 29.31),
        (
            "UnitedHealth Group",
            "Richard Burke, Bob Sheehy",
            "USA",
            "Minnesota",
            1977,
            400000,
            324.2,
        ),
    ],
)

# 提交變更並關閉連接
conn.commit()
conn.close()
