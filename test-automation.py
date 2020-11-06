import rpa as r

r.init(visual_automation = True)
r.url("http://google.com")
r.type(600, 300, 'open source')
r.click(900, 300)
r.snap('page.bmp', 'results.bmp')
r.hover('button_to_drag.bmp')
r.mouse('down')
r.hover(r.mouse_x() + 300, r.mouse_y())
r.mouse('up')
r.close()