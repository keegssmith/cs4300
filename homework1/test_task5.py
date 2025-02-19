from task5 import fav_books, students

def test_fav_books():
    assert fav_books() == [('Imaginary Friend', 'Stephen Chbosky'), ('Salt to the Sea', 'Ruta Sepetys'), ('The House Across the Lake', 'Riley Sager')]

def test_students():
    assert students() == {'Bob Smith': '1', 'Julia Roberts': '2', 'Dean Lucas': '3'}