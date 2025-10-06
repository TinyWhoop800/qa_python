import pytest
from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.books_genre) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    # Метод __init__
    def test_init_books_genre_is_empty_dict(self):
        collector = BooksCollector()
        assert collector.books_genre == {}
    
    def test_init_favorites_is_empty_list(self):
        collector = BooksCollector()
        assert collector.favorites == []
    
    def test_init_genre_contains_correct_items(self):
        collector = BooksCollector()
        expected_genres = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
        assert collector.genre == expected_genres
    
    def test_init_genre_age_rating_contains_correct_items(self):
        collector = BooksCollector()
        expected_genre_age_rating = ['Ужасы', 'Детективы']
        assert collector.genre_age_rating == expected_genre_age_rating
    
    # Метод add_new_book
    @pytest.mark.parametrize('positive_boundary_values', ['a','a' * 40])
    def test_add_new_book_can_add_books_with_boundary_name_lengths(self, positive_boundary_values):
        collector = BooksCollector()
        collector.add_new_book(positive_boundary_values)
        assert positive_boundary_values in collector.books_genre
        
    def test_add_new_book_has_empty_genre_after_adding(self):
        collector = BooksCollector()
        book_name = 'Test Book'
        collector.add_new_book(book_name)
        assert collector.books_genre[book_name] == ''
    
    @pytest.mark.parametrize('negative_boundary_values', ['', 'A' * 41])
    def test_add_new_book_cannot_add_books_with_invalid_boundary_name_lengths(self, negative_boundary_values):
        collector = BooksCollector()
        collector.add_new_book(negative_boundary_values)
        assert len(collector.books_genre) == 0
    
    def test_add_new_book_cannot_add_duplicate(self):
        collector = BooksCollector()
        book_name = "Дублирующаяся книга"
        collector.add_new_book(book_name)
        books_count = len(collector.books_genre)
        collector.add_new_book(book_name)
        assert len(collector.books_genre) == books_count
    
    # Метод set_book_genre
    @pytest.mark.parametrize('valide_genre', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_set_book_genre_can_set_all_valid_genres(self, valide_genre):
        collector = BooksCollector()
        book_name = 'Test Book'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, valide_genre)
        assert collector.books_genre[book_name] == valide_genre
    
    def test_set_book_genre_cannot_set_for_nonexistent_book(self):
        collector = BooksCollector()
        collector.set_book_genre('Несуществующая книга', 'Ужасы')
        assert len(collector.books_genre) == 0
    
    def test_set_book_genre_cannot_set_invalid_genre(self):
        collector = BooksCollector()
        book_name = 'Test Book'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, 'Несуществующий жанр')
        assert collector.books_genre[book_name] == ''
    
    # Метод get_book_genre
    def test_get_book_genre_returns_correct_genre(self):
        collector = BooksCollector()
        book_name = 'Test Book'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, 'Ужасы')
        assert collector.get_book_genre(book_name) == 'Ужасы'
    
    def test_get_book_genre_returns_empty_for_book_without_genre(self):
        collector = BooksCollector()
        book_name = 'Test Book'
        collector.add_new_book(book_name)
        assert collector.get_book_genre(book_name) == ''
    
    # Метод get_books_with_specific_genre
    def test_get_books_with_specific_genre_returns_correct_books(self):
        collector = BooksCollector()
        collector.add_new_book("Test Book")
        collector.set_book_genre("Test Book", "Фантастика")
        assert collector.get_books_with_specific_genre("Фантастика") == ["Test Book"]
    
    def test_get_books_with_specific_genre_returns_empty_list_for_genre_without_books(self):
        collector = BooksCollector()
        collector.add_new_book("Test Book")
        collector.set_book_genre("Test Book", "Фантастика")
        assert collector.get_books_with_specific_genre("Ужасы") == []
    
    def test_get_books_with_specific_genre_returns_multiple_books(self):
        collector = BooksCollector()
        collector.add_new_book("Book 1")
        collector.add_new_book("Book 2")
        collector.add_new_book("Book 3")
        collector.set_book_genre("Book 1", "Комедии")
        collector.set_book_genre("Book 2", "Комедии")
        collector.set_book_genre("Book 3", "Фантастика")
        collector.get_books_with_specific_genre("Комедии")
        
        assert collector.get_books_with_specific_genre("Комедии") == ["Book 1", "Book 2"]
    
    def test_get_books_with_specific_genre_returns_empty_for_invalid_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Test Book")
        collector.set_book_genre("Test Book", "Фантастика")
        assert collector.get_books_with_specific_genre("Несуществующий жанр") == []
    
    def test_get_books_with_specific_genre_returns_empty_for_empty_collection(self):
        collector = BooksCollector()
        assert collector.get_books_with_specific_genre("Фантастика") == []
    
    # Метод get_books_genre
    def test_get_books_genre_returns_actual_dict(self):
        collector = BooksCollector()
        assert collector.get_books_genre() is collector.books_genre
    
    # Метод get_books_for_children
    def test_get_books_for_children_returns_books_without_age_rating(self):
        collector = BooksCollector()
        collector.add_new_book("Book 1")
        collector.add_new_book("Book 2")
        collector.set_book_genre("Book 1", "Фантастика")
        collector.set_book_genre("Book 2", "Мультфильмы")
        assert collector.get_books_for_children() == ["Book 1", "Book 2"]

    def test_get_books_for_children_excludes_books_with_age_rating(self):
        collector = BooksCollector()
        collector.add_new_book("Book 1")
        collector.add_new_book("Book 2")
        collector.set_book_genre("Book 1", "Ужасы")
        collector.set_book_genre("Book 2", "Детективы")
        assert collector.get_books_for_children() == []

    def test_get_books_for_children_excludes_books_without_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Book 1")
        collector.add_new_book("Book 2")
        collector.set_book_genre("Book 2", "Фантастика")
        assert collector.get_books_for_children() == ["Book 2"]

    def test_get_books_for_children_returns_empty_list_when_no_suitable_books(self):
        collector = BooksCollector()
        assert collector.get_books_for_children() == []
    
    # Метод add_book_in_favorites
    def test_add_book_in_favorites_adds_existing_book(self):
        collector = BooksCollector()
        collector.add_new_book("Book 1")
        collector.add_book_in_favorites("Book 1")
        assert collector.favorites == ['Book 1']
    
    def test_add_book_in_favorites_cannot_add_nonexistent_book(self):
        collector = BooksCollector()
        collector.add_book_in_favorites("Book 1")
        assert collector.favorites != ['Book 1']
    
    def test_add_book_in_favorites_cannot_add_duplicate(self):
        collector = BooksCollector()
        collector.add_new_book("Book 1")
        collector.add_book_in_favorites("Book 1")
        collector.add_book_in_favorites("Book 1")
        assert len(collector.favorites) == 1
    
    # Метод delete_book_from_favorites
    def test_delete_book_from_favorites_removes_existing_book(self):
        collector = BooksCollector()
        collector.add_new_book("Book 1")
        collector.add_book_in_favorites("Book 1")
        collector.delete_book_from_favorites("Book 1")
        assert len(collector.favorites) == 0
    
    def test_delete_book_from_favorites_ignores_nonexistent_book(self):
        collector = BooksCollector()
        collector.add_new_book("Book 1")
        collector.add_book_in_favorites("Book 1")
        collector.delete_book_from_favorites("Book 2")
        assert len(collector.favorites) == 1
    
    def test_delete_book_from_favorites_removes_only_specified_book(self):
        collector = BooksCollector()
        collector.add_new_book("Book 1")
        collector.add_new_book("Book 2")
        collector.add_new_book("Book 3")
        collector.add_book_in_favorites("Book 1")
        collector.add_book_in_favorites("Book 2")
        collector.add_book_in_favorites("Book 3")
        collector.delete_book_from_favorites("Book 3")
        assert collector.favorites == ['Book 1', 'Book 2']
    
    # Метод get_list_of_favorites_books
    def test_get_list_of_favorites_books_returns_actual_favorites_list(self):
        collector = BooksCollector()
        assert collector.get_list_of_favorites_books() is collector.favorites

    def test_get_list_of_favorites_books_returns_books_after_adding(self):
        collector = BooksCollector()
        collector.add_new_book("Книга 1")
        collector.add_new_book("Книга 2")
        collector.add_book_in_favorites("Книга 1")
        collector.add_book_in_favorites("Книга 2")
        assert collector.get_list_of_favorites_books() == ["Книга 1", "Книга 2"]