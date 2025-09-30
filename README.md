# qa_python
Тесты метода __init__:
    1. test_init_books_genre_is_empty_dict - books_genre является пустым словарем
    2. test_init_favorites_is_empty_list - favorites является пустым списком
    3. test_init_genre_contains_correct_items - genre содержит ожидаемые жанры
    4. test_init_genre_age_rating_contains_correct_items - genre_age_rating содержит ожидаемые возрастные жанры

Тесты метода add_new_book:
    1. test_add_new_book_can_add_books_with_boundary_name_lengths - позитивные граничные значения (1, 40) при добавлении новой книги
    2. test_add_new_book_cannot_add_books_with_invalid_boundary_name_lengths - негативные граничные значения (0, 41) при добавлении новой книги
    3. test_add_new_book_has_empty_genre_after_adding - при добавлении новой книги жанр не присваивается
    4. test_add_new_book_cannot_add_duplicate - дублирущая книга не добавляется

Тесты метода set_book_genre:
    1. test_set_book_genre_can_set_all_valid_genres - добавление жанров к книге
    2. test_set_book_genre_cannot_set_for_nonexistent_book - добавление жанра к несуществующей книге
    3. test_set_book_genre_cannot_set_invalid_genre - попытка добавить несуществующий жанр

Тесты метода get_book_genre:
    1. test_get_book_genre_returns_correct_genre - получение существующего жанра
    2. test_get_book_genre_returns_empty_for_book_without_genre - проверка книги без жанра

Тесты метода get_books_with_specific_genre:
    1. test_get_books_with_specific_genre_returns_correct_books - получаем список книг по жанру
    2. test_get_books_with_specific_genre_returns_empty_list_for_genre_without_books - пустой список для валидного жанра, но без книг
    3. test_get_books_with_specific_genre_returns_multiple_books - возвращает несколько книг одного жанра
    4. test_get_books_with_specific_genre_returns_empty_for_invalid_genre - пустой список для невалидного жанра
    5. test_get_books_with_specific_genre_returns_empty_for_empty_collection - пустой список, когда в жанре нет книг

Тесты метода get_books_genre:
    1. test_get_books_genre_returns_actual_dict - возвращает актуальный словарь books_genre

Тесты метода get_books_for_children:
    1. test_get_books_for_children_returns_books_without_age_rating - книги без возрастных ограничений
    2. test_get_books_for_children_excludes_books_with_age_rating - книги с возрастными ограничениями
    3. test_get_books_for_children_excludes_books_without_genre - книги без жанра нет в списке
    4. test_get_books_for_children_returns_empty_list_when_no_suitable_books - книг нет в принципе

Тесты метода add_book_in_favorites:
    1. test_add_book_in_favorites_adds_existing_book - добавляет существующую книгу в избранное
    2. test_add_book_in_favorites_cannot_add_nonexistent_book - не добавляет несуществующую книгу в избранное
    3. test_add_book_in_favorites_cannot_add_duplicate - не добавляет дубликаты в избранное

Тесты метода delete_book_from_favorites:
    1. test_delete_book_from_favorites_removes_existing_book - удаляет существующую книгу
    2. test_delete_book_from_favorites_ignores_nonexistent_book - попытка удалить несуществующую книгу
    3. test_delete_book_from_favorites_removes_only_specified_book - при удалении одной книги из избранного, другие остаются

Тесты метода get_list_of_favorites_books:
    1. test_get_list_of_favorites_books_returns_actual_favorites_list - возвращает список избранного
    2. test_get_list_of_favorites_books_returns_books_after_adding - возвращает книги после добавления в избранное