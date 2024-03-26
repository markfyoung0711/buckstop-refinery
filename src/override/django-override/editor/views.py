from django.shortcuts import render
from editor.models import Override


# Create your views here.
def display_editor(request):
    return render(request=request, template_name="editor/index.html")


def all_overrides(request):
    # query the database to return all overrides
    overrides = Override.objects.all()
    print(all)
    return render(
        request=request,
        template_name="editor/all_overrides.html",
        context={"overrides": overrides},
    )
