from .models import ChoiceProductCategory, Product


class DataMixin:
    paginate_by = 8

    def get_user_context(self, **kwargs):
        context = kwargs
        category_choice = ChoiceProductCategory.objects.all()

        context['category_choice'] = category_choice
        if 'category_choice_selected' not in context:
            context['category_choice_selected'] = 0
        return context
