import PyPDF2
from tika import parser
import codecs
import re


def getPDFContent(path):
    content = ""
    # Load PDF into pyPDF
    s = u'Capit\xe1n\n'
    sutf8 = s.encode('UTF-8')

    f = codecs.open('file_name.txt', 'rb', 'UTF-8')
    pdf = PyPDF2.PdfFileReader(f)
    # Iterate pages

    for i in range(pdf.getNumPages()):
        # Extract text from page and add to content
        content += pdf.getPage(i).extractText() + "\n"
    # Collapse whitespace
    content = " ".join(content.replace("\xa0", " ").strip().split())
    return content


def getText(path):
    profile = open(path,'r' , errors='ignore')
    text = ""

    for line in profile:
        text += line

    profile.close()
    return text

def find_name(text):

    roots_text = 'Nguyễn	Trần	Lê	Phạm Hoàng Huỳnh	Phan	Vũ Võ	Đặng	Bùi	Đỗ	Hồ	Ngô	Dương	Lý \
    An	Ánh	Ân	Âu	Ấu	Bá	Bạc	Bạch	Bàn	Bàng	Bành	Bảo Bửu \
    Bế	Bì	Biện	Bình	Bồ	Ca	Cái	Cam	Cao	Cát	Cầm	Cấn \
    Cảnh	Chế	Chiêm	Chu Châu	Chung Trung	Chúng	Chương	Chử	Cổ	Cù	Cung	Cự\
    Dã	Danh	Diêm	Diệp	Doãn	Dư	Đàm	Đan	Đào	Đậu	Điền	Đinh\
    Đoàn	Đôn	Đồng	Đổng	Đới Đái	Đức	Đường	Giả	Giao	Giang	Giàng	Giáp\
    Hà	Hạ	Hàn	Hán	Hề Hè	Hi	Hình	Hoa	Hồng	Hùng	Hứa	Hướng\
    Kha	Khương	Khâu Khưu	Khiếu	Khoa	Khổng	Khu	Khuất	Khúc	Kiều	Kim	La\
    Lạc	Lại	Lâm	Lều	Lãnh Lăng	Liễu	Lò Lô	Lỗ	Luyện	Lục	Lư	Lữ Lã\
    Lương	Lưu  Lỳ	Lý	Ma	Mã	Mạc	Mạch	Mai	Mang	Mâu	Mẫn	Mộc\
    Ninh	Nhâm	Ngân	Nghiêm	Nghị	Ngọ	Ngụy	Nhữ	Nông	Ong	Ông	Phi\
    Phí	Phó	Phú	Phùng	Phương Phường	Quản	Quàng	Quách	Sầm	Sơn	Sử	Tạ\
    Tào	Tán	Tăng	Thạch	Thái	Thành	Thào	Thẩm	Thân	Thập	Thi	Thiều	Thịnh\
    Thôi	Tiêu	Tiếp	Tòng	Tô	Tôn	Tông	Tống	Trang	Trà	Trác	Tri\
    Triệu	Trịnh	Trình	Trưng Trừng	Trương	Từ	Ti	Uông	Ung	Ưng	Ứng	Văn\
    Vi	Viên	Vương  Vừ	Xa	Yên	Ngọc	Liêu	Thoa'

    if len(text.split()) > 4:
        return None

    for root in roots_text.split():
            list_root = text.strip().split()

            if root in list_root:
                return text
            else:
                pass
    return None


def find_location(text):
    provines =  ['An Giang', 'Bà Rịa - Vũng Tàu', 'Bắc Giang', 'Bắc Kạn', 'Bạc Liêu' ,'Bắc Ninh', 'Bến Tre', 'Bình Định'\
                , 'Bình Dương', 'Bình Phước', 'Bình Thuận', 'Cà Mau', 'Cao Bằng', 'Đắk Lắk', 'Đắk Nông', 'Điện Biên',
                 'Đồng Nai', 'Đồng Tháp', 'Gia Lai' ,'Hà Giang', 'Hà Nam', 'Hà Tĩnh', 'Hải Dương' ,'Hậu Giang', 'Hòa Bình',
                 'Hưng Yên', 'Khánh Hòa', 'Kiên Giang', 'Kon Tum', 'Lai Châu', 'Lâm Đồng', 'Lạng Sơn', 'Lào Cai', 'Long An',
                 'Nam Định','Nghệ An', 'Ninh Bình', 'Ninh Thuận', 'Phú Thọ','Quảng Bình', 'Quảng Nam', 'Quảng Ngãi', 'Quảng Ninh',
                 'Quảng Trị','Sóc Trăng', 'Sơn La', 'Tây Ninh', 'Thái Bình', 'Thái Nguyên', 'Thanh Hóa','Thừa Thiên Huế', 'Tiền Giang',
                 'Trà Vinh','Tuyên Quang', 'Vĩnh Long', 'Vĩnh Phúc', 'Yên Bái', 'Phú Yên','Cần Thơ', 'Đà Nẵng', 'Hải Phòng',
                 'Hà Nội', 'TP HCM']

    for provine in provines:
        for string in text.split("-"):
            if string is provine:
                print(string)
                return text
            else:
                pass

def find_birthday(date):
    regrex = r"^([1-9] |1[0-9]| 2[0-9]|3[0-1])(.|-)([1-9] |1[0-2])(.|-|)20[0-9][0-9]$"

    if re.match(regrex, date):
        return date

    return  None


def find_email(text):
    regrex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

    if re.match(regrex, text):
        return text
    return None


def isLineEmpty(line):
    return len(line.strip()) == 0


path = '/home/luanho/Downloads/Nguyen-Van-Son-CV.txt'
content = getText(path)




for line in content.split('\n'):

    if not isLineEmpty(line):
        #print(line)
        if (find_name(line) != None):
            print("Ho ten : " + line)

        if(find_location(line) != None):
            print("Dia chi : " + line)

        if find_email(line) != None:
            print("Email : " + line)

        if(find_birthday(line) != None):
            print(find_birthday(line))
