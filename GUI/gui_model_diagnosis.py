class UI_Diagnosis():
	def __init__(self):
		#Tab 1
		self.xingming = ''
		self.xingbie = ''
		self.zhiye = ''
		self.minzu = ''
		self.jiatingzhuzhi = ''
		self.wenhuachengdu = ''
		#Tab 2 
		self.zhongliubingshicunzai = ''
		self.zhongliubingshineirong = ''
		self.feijiehebingshicunzai = ''
		self.feijiehebingshineirong = ''
		self.fenchenxirushicunzai = ''
		self.xirugongzuonianxian = ''
		self.gongzhong = ''
		self.yichuanbingshicunzai = ''
		self.yichuanbingshineirong = ''
		self.xiyanshicunzai = ''
		self.xiyannianxian = ''
		self.meitianxiyanzhishu = ''
		self.huxibingshihuoqitacunzai = ''
		self.huxibingshihuoqitaneirong = ''
		#Tab 3
		self.zhusu = ''
		self.fare = ''
		self.kesou = ''
		self.tanzhongdaixue = ''
		self.kexue = ''
		self.xiongmen = ''
		self.xiongtong = ''
		self.shengyinsiya = ''
		self.qitayuhuxiyouguandelinchuangbiaoxian = ''
		self.linchuangzhenduanyijian = ''
		#Tab 4
		self.CThao = ''
		self.jianchafangshi = ''
		self.jianchariqi = ''
		self.jiejiedaxiao = ''
		self.jiejiebuwei = ''
		self.linbajiezhong = ''
		self.jiejiemidu = ''
		self.maobolimi = ''
		self.shixingjiejie = ''
		self.jiejiebianyuan = ''
		self.youyunzheng = ''
		self.jiejiekongpao = ''
		self.jiejiefenye = ''
		self.kongdong = ''
		self.jiejiegaihua = ''
		self.xiongshui = ''
		self.xiongmoaoxian = ''
		self.CTzhenduan = ''

		#Others
		self.images = []
		#[001,002,003]
		#(image_feature + pat_info)
		self.probability_of_illness = ''
		
	def __str__(self):
		items = [x+":"+str(getattr(self, x))  for x in dir(self)]
		return "\n".join(items)
		