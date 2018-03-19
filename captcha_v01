#coding:utf-8
from PIL import Image
import math ,os



#定义矢量比较
class VectorCompare:
	def magnitude(self , dic):
		summ = 0
		for k,v in dic.iteritems():
			summ += v * v
		return math.sqrt(summ)

	def relation(self, dic1 , dic2):
		mid = 0
		for k,v in dic1.iteritems():
			if dic2.has_key(k):
				mid += v * dic2[k]
		return mid / self.magnitude(dic1) / self.magnitude(dic2)


#图像转化为矢量
def buildvector(im):
	return {i:j for i,j in enumerate(im.getdata())}

class captcha():

        
    #读取训练库中的图像
    def trainingset(self):
        self.store = {}
        for l in '0123456789abcdefghijklmnopqrstuvwxyz':
                try:
                    self.store[l] = [buildvector(Image.open('./iconset/%s/%s'%(l,img))) for img in os.listdir('./iconset/%s/'%l) if img != 'Thumbs.db' and img != '.DS_Store']
                except IOError:
                    print l,img
                #except StandardError as e:
                     
                    return False

        return True


    def __init__(self , source):    #验证码文件
            
            self.im = Image.open(source)
            self.im.convert('P')		#格式转换 1/二值图像，L/灰度图像，P/8位彩色，RGB，RGBA，CMYK，YCbCr，I/32位整型灰图，F/32位浮点灰图
            self.im2 = Image.new('P',self.im.size,255)

            mid = self.im.histogram()	#查看通道直方图
            values = dict(zip(range(len(mid)),mid))
            if not self.trainingset():
                print 'training set not ready. program exits!'
                exit()


    #生成验证码的二值图像（有效色与背景色已选定）
    def segment(self):
        
        for x in range(self.im.size[0]):
                for y in range(self.im.size[1]):
                        pix = self.im.getpixel((x,y))
                        if pix == 220 or pix == 227:
                                self.im2.putpixel((x,y),0)

                            
        #分割验证码图像，确定每个字符的大致区间
        
        start = -1
        letters = []
        for x in range(self.im2.size[0]):
                for y in range(self.im2.size[1]):
                        if self.im2.getpixel((x,y)) != 255:
                                if start >= 0:
                                        break
                                else:
                                        start = x
                                        break
                        elif y + 1 == self.im2.size[1] and start >= 0:
                                letters.append((start,x))
                                start = -1
        return letters


    #验证码图像局部识别
    def recognize(self):
        res = ''
        vp = VectorCompare()
        for letter in self.segment():
                im3 = self.im2.crop((letter[0], 0 , letter[1] , self.im2.size[1]))
                imv = buildvector(im3)
                glist = {}
                for guessfrom in self.store.keys():
                        glist[guessfrom] = max(map(lambda x:vp.relation(x,imv),self.store[guessfrom]))
                res += sorted(glist.iteritems(),key=lambda x:x[1],reverse=True)[0][0]
        return res


if __name__ == '__main__':
    example = captcha('captcha.gif')
    print example.recognize()

    for f in os.listdir('./examples/'):
        
        if f[-3:] == 'gif':
            mid = captcha('./examples/%s'%f).recognize()
            print '{0} ---> {1}   {2}'.format(f,mid,str(mid in f))
    
