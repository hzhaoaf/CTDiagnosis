class SingleImageItem:
	def __init__(self,origin = None,cropped = None,region_growed = None,is_in_use = True):
		self._origin = origin
		self._cropped = cropped
		self._region_growed = region_growed
		self._is_in_use = is_in_use
	def is_in_use(self):
		return self._is_in_use
	
	def enable(self,enable):
		self._is_in_use = enable
		
	def get_item_prior_file(self):
		if self._region_growed:return self._region_growed
		if self._cropped:return self._cropped
		if self._origin:return self._origin
		return None
	
	def do_regiongrow(self,file_name):
		self._region_growed = file_name
		
	def do_crop(self,file_name):
		self._cropped = file_name
		
class ImageItemsList:
	def __init__(self):
		self._number_of_items = -1
		self._current_item_no = -1
		self._image_items = []
		
	def init_list(self,paths):
		self._number_of_items = len(paths)
		self._current_item_no = 0
		self._image_items = [SingleImageItem(origin=p) for p in paths]
		
	def is_current_image_in_use(self):
		if self._number_of_items <= 0:
			return False
		return self._image_items[self._current_item_no].is_in_use()
		
	def do_current_image_regiongrow(self,file_name):
		self._image_items[self._current_item_no].do_regiongrow(file_name)	
	def do_current_image_crop(self,file_name):
		self._image_items[self._current_item_no].do_crop(file_name)
		
	def get_current_image_file(self):
		if self._number_of_items <= 0:
			return None
		return self._image_items[self._current_item_no].get_item_prior_file()
	
	def append_item(self,origin_file_name):
		sii = SingleImageItem(origin=origin_file_name)
		self._image_items.append(sii)
		self._number_of_items += 1
		
	def get_next_image_file_name(self):
		if self._number_of_items <= 0 or self._current_item_no+1 > self._number_of_items -1:
			return None
		self._current_item_no += 1
		return self._image_items[self._current_item_no].get_item_prior_file()

	def get_prev_image_file_name(self):
		if self._number_of_items <= 0 or self._current_item_no - 1 < 0:
			return None
		self._current_item_no -= 1
		return self._image_items[self._current_item_no].get_item_prior_file()
	
	def get_all_enable_images_path(self):
		return [s.get_item_prior_file() for s in self._image_items if s.is_in_use()]
	
	def do_enable_current_image(self,enable):
		self._image_items[self._current_item_no].enable(enable)