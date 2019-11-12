from django.shortcuts import render
from wiki.models import Page
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .forms import PageForm
from django.http import HttpResponseRedirect




class PageList(ListView):
    """
    Renders the list of pages view.
    """
    model = Page
    template_name = 'wiki/list.html'
    context_object_name = 'pages'

    # def get(self, request):
    #     """ Returns a list of wiki pages. """
    #     all_pages = Page.objects.all()
    #     context = {
    #       'page_list': all_pages,
    #     }
    #     return render(request, 'wiki/list.html', context)


class PageDetailView(DetailView):
    """
    Render the individual page view.

    STRETCH CHALLENGES:
      1. Import the PageForm class from forms.py.
          - This ModelForm enables editing of an existing Page object in the database.
      2. On GET, render an edit form below the page details.
      3. On POST, check if the data in the form is valid.
        - If True, save the data, and redirect back to the DetailsView.
        - If False, display all the errors in the template, above the form fields.
      4. Instead of hard-coding the path to redirect to, use the `reverse` function to return the path.
      5. After successfully editing a Page, use Django Messages to "flash" the user a success message
           - Message Content: REPLACE_WITH_PAGE_TITLE has been successfully updated.
    """
    model = Page
    template_name = 'wiki/page.html'
    context_object_name = 'page'

    # def get(self, request, slug):
    #     """ Returns a specific of wiki page by slug. """
    #     page = Page.objects.get(slug=slug) # slug is name of parameter
    #     context = {
    #       'page': page,
    #     }
    #     return render(request, 'wiki/page.html', context)

    def post(self, request, slug):
        if request.method == 'POST':
          form = PageForm(request.POST)

          if form.is_valid():
            return HttpResponseRedirect('/thanks/')

        else:
            form = PageForm()

        return render(request, 'wiki/page.html', {'form':form})

