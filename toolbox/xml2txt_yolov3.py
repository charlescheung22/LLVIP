import os
import argparse
import xml.etree.ElementTree as ET
from tqdm import tqdm


def parse_opt():
    parser = argparse.ArgumentParser(description='Convert LLVIP XML annotations to YOLO format in single txt file')
    parser.add_argument('--annotation_path', type=str,
                        default='/home/dataset/LLVIP/Annotations',
                        help='folder containing xml files')
    parser.add_argument('--image_path', type=str, default='/home/dataset/LLVIP/infrared/train',
                        help='image path, e.g. /root/LLVIP/infrared/train')
    parser.add_argument('--txt_path', type=str, default='/home/dataset/LLVIP/labels/a.txt',
                        help='saving all bboxes of all images to a txt file')
    opt = parser.parse_args()
    return opt


opt = parse_opt()


def convert_LLVIP_annotation(anno_path, image_path, txt_path):
    # 创建保存txt文件的目录
    os.makedirs(os.path.dirname(txt_path), exist_ok=True)

    # 清空并创建txt文件
    with open(txt_path, 'w') as f:
        pass

    # 获取所有图像文件名
    image_files = os.listdir(image_path)

    for i in tqdm(image_files):
        try:
            # 获取图像文件名(不含扩展名)
            img_name = i.split(".")[0]

            # 构建对应的XML文件路径
            xml_file = os.path.join(anno_path, img_name + '.xml')

            # 检查XML文件是否存在
            if not os.path.exists(xml_file):
                print(f"警告: {xml_file} 不存在，跳过")
                continue

            # 解析XML文件
            tree = ET.parse(xml_file)
            root = tree.getroot()

            # 获取所有对象
            objects = root.findall('object')

            # 构建当前图像的标注行
            annotation = os.path.join(image_path, i)

            # 处理每个对象
            for obj in objects:
                try:
                    # 获取边界框坐标
                    bbox = obj.find('bndbox')
                    xmin = int(bbox.find('xmin').text.strip())
                    ymin = int(bbox.find('ymin').text.strip())
                    xmax = int(bbox.find('xmax').text.strip())
                    ymax = int(bbox.find('ymax').text.strip())

                    # 添加边界框信息到标注行
                    annotation += f' {xmin},{ymin},{xmax},{ymax},0'
                except Exception as e:
                    print(f"警告: 处理 {xml_file} 中的对象时出错: {e}")
                    continue

            # 将标注行写入txt文件
            with open(txt_path, 'a') as f:
                f.write(annotation + "\n")

        except Exception as e:
            print(f"错误: 处理文件 {i} 时出错: {e}")
            continue


anno_path = opt.annotation_path
image_path = opt.image_path
txt_path = opt.txt_path
convert_LLVIP_annotation(anno_path, image_path, txt_path)