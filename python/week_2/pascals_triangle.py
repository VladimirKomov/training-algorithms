def build_list(n):
    print(f"Вход в build_list({n})")  # ← следим, когда функция вызвана

    if n == 0:
        print("  Базовый случай: возвращаю []")
        return []

    result = build_list(n - 1)
    final_result = result + [n]

    print(f"  build_list({n - 1}) вернул {result}, добавляем {n} → {final_result}")
    return final_result




if __name__ == '__main__':
    print(build_list(3))
