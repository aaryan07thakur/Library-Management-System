from django.db import models

# Create your models here.

#for USers
class User(models.Model):
    UserID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Email = models.EmailField(unique=True)
    MembershipDate = models.DateField()

    def __str__(self):
        return self.Name

#for Books
class Book(models.Model):
    BookID = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=200)
    ISBN = models.CharField(max_length=13, unique=True)
    PublishedDate = models.DateField()
    Genre = models.CharField(max_length=50)

    def __str__(self):
        return self.Title
    
#BooksDetails:
class BookDetails(models.Model):
    DetailsID = models.AutoField(primary_key=True)
    BookID = models.OneToOneField(Book, on_delete=models.CASCADE)
    NumberOfPages = models.IntegerField()
    Publisher = models.CharField(max_length=100)
    Language = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.BookID.Title} - Details"

#for Borrowed Books    
class BorrowedBooks(models.Model):
    UserID = models.ForeignKey(User, on_delete=models.CASCADE)
    BookID = models.ForeignKey(Book, on_delete=models.CASCADE)
    BorrowDate = models.DateField()
    ReturnDate = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.UserID.Name} - {self.BookID.Title}"