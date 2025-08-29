#!/usr/bin/env python3
"""
Простий Python додаток для тестування Docker
"""
import time
import datetime
import os


def main():
    print("🐳 Docker + Python = DevOps Magic!")
    print(f"📅 Поточний час: {datetime.datetime.now()}")
    print(f"🖥️  Hostname: {os.uname().nodename}")
    print(f"👤 User: {os.getenv('USER', 'unknown')}")

    # Простий лічильник
    counter = 0
    try:
        while True:
            counter += 1
            print(f"🔄 Лічильник: {counter}")
            time.sleep(5)

            if counter >= 10:
                print("✅ Додаток завершено успішно!")
                break

    except KeyboardInterrupt:
        print("\n⏹️ Додаток зупинено користувачем")


if __name__ == "__main__":
    main()