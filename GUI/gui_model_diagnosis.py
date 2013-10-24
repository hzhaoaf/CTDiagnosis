# -*- coding: utf-8 -*-
class PredictDiagnosis():
	def __init__(self):
		self.linchuangzhenduanyijian = ""
		self.xingbie  =""
		self.nianling = ""
		self.zhongliubingshicunzai = ""
		self.feijiehebingshicunzai = ""
		self.fenchenxirushicunzai = ""
		self.yichuanbingshicunzai = ""
		self.xiyanshicunzai = ""
		self.linbajiezhong= ""
		self.jiejiebuwei = ""
		self.jiejiedaxiao = ""
		self.jiejiemidu = ""
		self.shixingjiejie = ""
		self.maobolimi = ""
		self.jiejiebianyuan = ""
		self.jiejiefenye = ""
		self.jiejiekongpao = ""
		self.jiejiegaihua = ""
		self.kongdong = ""
		self.xiongmoaoxian = ""
		self.xiongshui = ""
	def __str__(self):
		items = [x+":"+str(getattr(self, x))  for x in dir(self)]
		return "\n".join(items)	

class UI_Diagnosis():
	def __init__(self):
		#Tab 1
		self.xingming = ''
		self.xingbie = ''
		self.nianling = ''
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
		self.jiejiebuwei = ''#左肺上叶(0) 左肺下叶(1) 右肺上叶(2) 右肺中叶(3) 右肺下叶(4)
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
	
	def normalize(self):
		pd = PredictDiagnosis()
		#pd.linchuangzhenduanyijian = self.linchuangzhenduanyijian
		pd.xingbie = 0 + 1 * (self.xingbie.decode('utf8') == u"女")
		pd.nianling = int(self.nianling) if self.nianling.isdigit() else 0 #promise this is a digit number
		pd.zhongliubingshicunzai = 0 + 1 * (self.zhongliubingshicunzai.decode('utf8') == u"有")
		pd.feijiehebingshicunzai = 0 + 1 * (self.feijiehebingshicunzai.decode('utf8') == u"有")
		pd.fenchenxirushicunzai = 0 + 1 * (self.fenchenxirushicunzai.decode('utf8') == u"有")
		pd.yichuanbingshicunzai = 0 + 1 * (self.yichuanbingshicunzai.decode('utf8') == u"有")
		pd.xiyanshicunzai =  0 + 1 * (self.xiyanshicunzai.decode('utf8') == u"有")
		pd.linbajiezhong = int(self.linbajiezhong) if self.linbajiezhong else 0
		
		#0=左肺下叶 或右肺中叶 或右肺下叶； 1=左肺上叶(0) 或右肺上叶(2)
		pd.jiejiebuwei = 1 if ('0' in self.jiejiebuwei or '2' in self.jiejiebuwei) else 0
		
		#If cannot converse a string to a float,set it to 0.
		try:
			pd.jiejiedaxiao = float(self.jiejiedaxiao)
		except:
			pd.jiejiedaxiao = 0	

		pd.jiejiemidu = int(self.jiejiemidu) if self.jiejiemidu else 0
		pd.shixingjiejie = int(self.shixingjiejie) if self.shixingjiejie else 0
		pd.maobolimi = int(self.maobolimi) if self.maobolimi else 0
		pd.jiejiebianyuan = int(self.jiejiebianyuan) if self.jiejiebianyuan else 0
		pd.jiejiefenye = int(self.jiejiefenye) if self.jiejiefenye else 0
		pd.jiejiekongpao = int(self.jiejiekongpao) if self.jiejiekongpao else 0
		pd.jiejiegaihua = int(self.jiejiegaihua) if self.jiejiegaihua else 0
		pd.kongdong = int(self.kongdong) if self.kongdong else 0
		pd.xiongmoaoxian = int(self.xiongmoaoxian) if self.xiongmoaoxian else 0
		pd.xiongshui = int(self.xiongshui)if self.xiongshui else 0
		print(pd)


	def __str__(self):
		items = [x+":"+str(getattr(self, x))  for x in dir(self)]
		return "\n".join(items)
		