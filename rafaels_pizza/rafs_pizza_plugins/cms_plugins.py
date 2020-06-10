from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from .models import Daily_Specials, Menu_Item


@plugin_pool.register_plugin
class Daily_Specials_Plugin(CMSPluginBase):
    model = Daily_Specials
    name = "Daily Sepecials"
    render_template = "daily_special.html"
    cache = False

    def render(self, context, instance, placeholder):
        context.update({
            'name': instance.name,
            'image': instance.image,
            'description': instance.description,
            'url': instance.url
        })
        return context


@plugin_pool.register_plugin
class Menu_Item_Plugin(CMSPluginBase):
    model = Menu_Item
    name = "Menu Item"
    render_template = "menu_item.html"
    cache = False

    def render(self, context, instance, placeholder):
        context.update({
            'name': instance.name,
            'image': instance.image,
            'price': instance.price,
            'description': instance.description,
            'url': instance.url
        })
        return context
