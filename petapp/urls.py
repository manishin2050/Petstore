from django.urls import path
from petapp import views

urlpatterns = [
    path('', views.home),
    path('login/', views.log_in),
    path('logout/', views.log_out),
    path('signup/', views.sign_up),
    path('about/<int:id>', views.about),
    path('cart/<int:id>', views.cart),
    path('buyCart/<int:pet_id>', views.payment),
    path('autoBuyCart/<int:pet_id>', views.buyCart),
    path('deleteCart/<int:id>', views.deleteCart),
    path('buy/<int:id>', views.buy),
    path('orderByName/',views.orderByName),
    path('orderByPrice/',views.orderByPrice),


    path('deleteOrder/<int:id>', views.deleteOrder),
    path('yourOrder/', views.yourOrder),
    path('cartItem/', views.cartItem),
    path('addpet/', views.addpet),
    path('search/',views.search),
    path('dog/',views.dog),
    path('cat/',views.cat),
    path('snake/',views.snake),
    path('bird/',views.bird),
    path('lizard/',views.lizard),
    path('cow/',views.cow),
    path('cock/',views.cock),
    path('goat/',views.goat),
    path('buffalo/',views.buffalo),
    path('wolf/',views.wolf),
    path('bear/',views.bear),
    path('json/',views.CreateJson),
    # path('cate/',views.cate),

]
