from fanstatic import Library, Resource, Group
from js.jquery import jquery

library = Library('jquery.colorpicker', 'resources')

def render_image(url):
    return ('')

from fanstatic.core import register_inclusion_renderer

register_inclusion_renderer('.png', render_image, 90)
register_inclusion_renderer('.gif', render_image, 90)

jquery_colorpicker_main_css         = Resource(library, 'css/colorpicker.css')

jquery_colorpicker_eye_js           = Resource(library, 'js/eye.js')
jquery_colorpicker_layout_js        = Resource(library, 'js/layout.js')
jquery_colorpicker_utils_js         = Resource(library, 'js/utils.js' )

jquery_colorpicker_img_background   = Resource(library, 'images/colorpicker_background.png')
jquery_colorpicker_img_overlay      = Resource(library, 'images/colorpicker_overlay.png')
jquery_colorpicker_img_indic        = Resource(library, 'images/colorpicker_indic.gif')
jquery_colorpicker_img_select       = Resource(library, 'images/colorpicker_select.gif')
jquery_colorpicker_img_hex          = Resource(library, 'images/colorpicker_hex.png')
jquery_colorpicker_img_rgb_r        = Resource(library, 'images/colorpicker_rgb_r.png')
jquery_colorpicker_img_rgb_b        = Resource(library, 'images/colorpicker_rgb_b.png')
jquery_colorpicker_img_rgb_g        = Resource(library, 'images/colorpicker_rgb_g.png')
jquery_colorpicker_img_hsb_h        = Resource(library, 'images/colorpicker_hsb_h.png')
jquery_colorpicker_img_hsb_s        = Resource(library, 'images/colorpicker_hsb_s.png')
jquery_colorpicker_img_submit       = Resource(library, 'images/colorpicker_submit.png')
jquery_colorpicker_img_hsb_b        = Resource(library, 'images/colorpicker_hsb_b.png')

jquery_colorpicker_javascripts      = Group([jquery_colorpicker_eye_js, jquery_colorpicker_layout_js, jquery_colorpicker_utils_js])
jquery_colorpicker_images           = Group([jquery_colorpicker_img_background, jquery_colorpicker_img_overlay,jquery_colorpicker_img_indic, jquery_colorpicker_img_select, jquery_colorpicker_img_hex, jquery_colorpicker_img_rgb_r, jquery_colorpicker_img_rgb_b, jquery_colorpicker_img_rgb_g, jquery_colorpicker_img_hsb_h, jquery_colorpicker_img_hsb_s, jquery_colorpicker_img_submit, jquery_colorpicker_img_hsb_b,])

jquery_colorpicker                  = Resource(
    library, 
    'js/colorpicker.js',
    depends=[jquery, jquery_colorpicker_main_css, jquery_colorpicker_javascripts, jquery_colorpicker_images]
)
