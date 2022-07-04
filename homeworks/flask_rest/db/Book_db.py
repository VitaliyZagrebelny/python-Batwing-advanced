class BookDB:
    books = [{"name": "Kobzar", "author": "Taras Shevchenko", "id": 1}]

    def get_all(self):
        return self.books

    def retrieve_by_id(self, id):
        try:
            book_id = int(id)
            for book in self.books:
                if book["id"] == book_id:
                    result = book
                else:
                    result = ('No match', 400)
        except Exception:
            result = ('Wrong url', 400)
        return result

    def add(self, name, author):
        exist = False

        for book in self.books:
            if id == book['id']:
                exist = True

        if not exist:
            book = {
                "name": name,
                "author": author,
                "id": self.books[-1]['id'] + 1
            }
            self.books.append(book)
            return book
        else:
            return False

    def update_by_id(self, name, id, author):
        try:
            int_id = int(id)
            for book in self.books:
                if book["id"] == int_id:
                    book['name'] = name
                    book['author'] = author
                    result = book
                    break
                else:
                    result = ("Book doesn't exists", 400)
        except Exception:
            result = ('Wrong url', 400)
        return result

    def delete_by_id(self, id):
        try:
            int_id = int(id)
            for book in self.books:
                if book["id"] == int_id:
                    self.books = [book for book in self.books if book["id"] != int_id]
                    result = 'Deleted'
                    break
                else:
                    result = ("Book doesn't exists", 400)
        except Exception:
            result = ('Wrong url', 400)
        return result
