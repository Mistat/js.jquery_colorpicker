from fanstatic import Library, Resource
from js.jquery import jquery

library = Library('jquery.colorpicker', 'resources')

jquery_colorpicker_main_css = Resource(
    library,
    'css/colorpicker.css'
)

jquery_colorpicker_eye_js = Resource(
    library,
    'js/eye.js'
)
jquery_colorpicker_layout_js = Resource(
    library,
    'js/layout.js'
)
jquery_colorpicker_utils_js = Resource(
    library,
    'js/utils.js'
)

jquery_colorpicker = Resource(
    library,
    'js/colorpicker.js',
    depends=[jquery, jquery_colorpicker_main_css, jquery_colorpicker_eye_js, jquery_colorpicker_layout_js, jquery_colorpicker_utils_js]
)
