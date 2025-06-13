import csv
import os

# book-log-manager/data/books.csv 경로 고정
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA_FILE = os.path.join(BASE_DIR, "data", "books.csv")

# 파일이 없으면 헤더 생성
def init_csv():
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, mode='w', newline='', encoding='utf-8-sig') as f:
            writer = csv.writer(f)
            writer.writerow(["제목", "작가", "감상"])

# 책 추가
def add_book():
    title = input("책 제목: ")
    author = input("작가: ")
    review = input("감상평: ")
    with open(DATA_FILE, mode='a', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        writer.writerow([title, author, review])
    print("✅ 책이 추가되었습니다.")

# 전체 목록 출력
def list_books():
    with open(DATA_FILE, mode='r', encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        books = list(reader)
        if len(books) <= 1:
            print("📭 저장된 책이 없습니다.")
            return
        print("\n=== 📚 책 목록 ===")
        for i, row in enumerate(books[1:], start=1):
            print(f"{i}. 제목: {row[0]} | 작가: {row[1]} | 감상: {row[2]}")

# 검색
def search_book():
    keyword = input("검색할 제목 또는 작가: ")
    with open(DATA_FILE, mode='r', encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        books = list(reader)
        results = [row for row in books[1:] if keyword in row[0] or keyword in row[1]]
        if results:
            print("\n🔍 검색 결과:")
            for row in results:
                print(f"제목: {row[0]} | 작가: {row[1]} | 감상: {row[2]}")
        else:
            print("❌ 해당하는 책을 찾을 수 없습니다.")

# 감상 수정
def update_review():
    title = input("감상을 수정할 책 제목: ")
    found = False
    with open(DATA_FILE, mode='r', encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        books = list(reader)
    for row in books[1:]:
        if row[0] == title:
            print(f"현재 감상: {row[2]}")
            row[2] = input("새 감상 입력: ")
            found = True
            break
    if found:
        with open(DATA_FILE, mode='w', newline='', encoding='utf-8-sig') as f:
            writer = csv.writer(f)
            writer.writerows(books)
        print("✏️ 감상이 수정되었습니다.")
    else:
        print("❌ 해당 제목의 책이 없습니다.")

# 책 삭제
def delete_book():
    title = input("삭제할 책 제목: ")
    with open(DATA_FILE, mode='r', encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        books = list(reader)
    new_books = [books[0]] + [row for row in books[1:] if row[0] != title]
    if len(books) == len(new_books):
        print("❌ 삭제할 책을 찾을 수 없습니다.")
    else:
        with open(DATA_FILE, mode='w', newline='', encoding='utf-8-sig') as f:
            writer = csv.writer(f)
            writer.writerows(new_books)
        print("🗑 책이 삭제되었습니다.")

# 메인 루프
def main():
    init_csv()
    while True:
        print("\n=== 📖 독서 기록 관리 시스템 ===")
        print("1. 책 추가")
        print("2. 목록 보기")
        print("3. 책 검색")
        print("4. 감상 수정")
        print("5. 책 삭제")
        print("0. 종료")
        choice = input("선택: ")

        if choice == '1':
            add_book()
        elif choice == '2':
            list_books()
        elif choice == '3':
            search_book()
        elif choice == '4':
            update_review()
        elif choice == '5':
            delete_book()
        elif choice == '0':
            print("📕 프로그램을 종료합니다.")
            break
        else:
            print("⚠️ 올바른 번호를 선택해주세요.")

if __name__ == '__main__':
    main()
