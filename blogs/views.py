from itertools import product

from django.db.models import Avg, Max, Min
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from datetime import date
from .models import Product
# Create your views here.
all_posts = [
    {"slug": "Python-Programming",
     "title": "Python.py",
     "author": "Mahdi",
     "date": date(1402, 5, 18),
     "image": "python.jpeg",
     "short_description": "Python is a high-level, general-purpose programming language",
     "content": """Python was conceived in the late 1980s[40] by Guido van Rossum at Cent rum Wunderkind & Informatica (
     CWI) in the Netherlands as a successor to the ABC programming language, which was inspired by SETL,[41] capable 
     of exception handling and interfacing with the Amoeba operating system.[10] Its implementation began in December 
     1989.[42] Van Rossum shouldered sole responsibility for the project, as the lead developer, until 12 July 2018, 
     when he announced his "permanent vacation" from his responsibilities as Python's "benevolent dictator for life", 
     a title the Python community bestowed upon him to reflect his long-term commitment as the project's chief 
     decision-maker.[43] In January 2019, active Python core developers elected a five-member Steering Council to 
     lead the project.[44][45]"""
     },
    {"slug": "C-Programming",
     "title": "C#",
     "author": "Mohammad",
     "date": date(1402, 12, 1),
     "image": "c#.png",
     "short_description": "a modern, object-oriented, and type-safe programming language",
     "content": """The C# programming language was designed by Anders Hejlsberg from Microsoft in 2000 and was later 
     approved as an international standard by Ecma (ECMA-334) in 2002 and ISO/IEC (ISO/IEC 23270 and 20619[c]) in 
     2003. Microsoft introduced C# along with"""
     },
    {"slug": "PHP-Programming",
     "title": "PHP",
     "author": "Bazari",
     "date": date(1402, 10, 23),
     "image": "php.png",
     "short_description": "PHP is a general-purpose scripting language geared towards web development",
     "content": """PHP is a general-purpose scripting language geared towards web development.[8] It was originally 
     created by Danish-Canadian programmer Rasmus Lerdorf in 1993 and released in 1995.[9][10] The PHP reference 
     implementation is now produced by the PHP Group.[11] PHP was originally an abbreviation of Personal Home Page,
     [12][13] but it now stands for the recursive initialism PHP: Hypertext Preprocessor.[14]"""
     },
]



def get_date(post):
    return post['date']
def index(request):
    # d = list(all_post)
    # context = {"a": d}
    # return render(request, 'blogs/index.html', context)
    post_sorted = sorted(all_posts, key=get_date)
    latests = post_sorted[-2:]
    return render(request, 'blogs/index.html', {'latests_posts': latests})
def posts(request):
    return render(request, 'blogs/all_post.html', {'all_post': all_posts})
def single_post(request, slug):
    post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, 'blogs/post_details.html', {'post': post})
def product_list(request):
    all_products = Product.objects.all().order_by('-price')
    numbers = all_products.count()
    info = all_products.aggregate(Avg("price"), Max("price"), Min("price"))
    return render(request, 'blogs/product_list.html', {'all_products': all_products, 'numbers': numbers, 'info': info})
def product_detail(request, slug):
    # try:
    #     p = Product.objects.get(id=product_id)
    # except:
    #     raise Http404
    p = get_object_or_404(Product, slug=slug)
    return render(request, 'blogs/product_details.html', {"p": p})
