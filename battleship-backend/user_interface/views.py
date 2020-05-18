from django.shortcuts import render

# Create your views here.
def main_game_view(request):
    rowCount = 10
    columnCount = 10

    rows = [x for x in range(0, rowCount)]
    columns = [x for x in range(0, columnCount)]



    return render(request, 'user_interface/main_page.html', {'rows': rows, 'columns': columns})