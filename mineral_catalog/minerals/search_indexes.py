from haystack import indexes
from minerals.models import Mineral


class MineralIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr='name')
    category = indexes.CharField(model_attr='category')
    group = indexes.CharField(model_attr='group')
    color = indexes.CharField(model_attr='color')

    def get_model(self):
        return Mineral

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(name__istartswith='A')
