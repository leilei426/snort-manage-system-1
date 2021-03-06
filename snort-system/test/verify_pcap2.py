# -*- coding: UTF-8 -*-
import re
import os


class GetHitRule(object):
    """
    获取命中上传的pcap的规则
    """

    def __init__(self):
        self.result_path = "/usr/suricata-4.0.0/log"
        self.result = []
        self.tips = ""
        self.sid_list = []
        self.result_list = []

    def read_result(self):
        """
        :describe:  读取命中结果文件
        :param:     类对象
        :return:    无
        """
        try:
            with open(os.path.join(self.result_path, 'fast.log')) as f:
                self.result_list = f.readlines()
                print self.result_list
        except IOError as e:
            print 'error:', e
        if len(self.result_list) > 0:
            self.result = self.result_list
            print self.result
        else:
            pass

    def judge_hit_rule(self):
        """
        :describe:  判断哪条规则命中
        :param:     类对象
        :return:    命中pcap的规则ID列表
        """
        sid_list = []
        hit_list = []
        if len(self.result) == 0:
            return None
        for i in range(len(self.result)):
            hit_result = self.result[i].split('[**]')[1]
            hit_rule_id = hit_result.split(']')[0].split(':')[1]
            print hit_rule_id
            hit_rule_name = hit_result.split(']')[1].strip()
            print hit_rule_name
            hit_dict = {hit_rule_id: hit_rule_name}
            hit_list.append(hit_dict)
            sid_list.append(hit_rule_id)
        # try:
        #     sid_list = re.findall(r'hit rules\:(.+?):', self.result)
        # except Exception as e:
        #     print 're find error:', e
        if len(sid_list) == 0:
            return None
        else:
            self.sid_list = sid_list
        return self.sid_list

    def get_hit_result(self):
        """
        :describe:  获取命中信息
        :param:     类对象
        :return:    命中规则描述
        """
        self.read_result()
        sid_list = self.judge_hit_rule()
        if sid_list is None:
            self.tips = '未命中任何规则!'
        else:
            self.tips = '命中%s号规则!' % self.sid_list
        return self.tips

    # def touch_result_file(self):
    #     """
    #     :describe:  创建存取结果的文件
    #     :param:     类对象
    #     :return:    无
    #     """
    #     get_file_cmd = 'touch ' + self.result_path
    #     os.system(get_file_cmd)

    def del_result_file(self):
        """
        :describe:  删除结果文件
        :param:     类对象
        :return:    无
        """
        cmd = 'rm -rf ' + self.result_path
        os.system(cmd)


def check_pcap_rules(pcap_path):
    # type: (object) -> object
    """
    :describe:  调用检测工具,获取结果
    :param:     上传的pcap文件路径
    :return:    无
    """
    cmd = './tool/test_tool ./all.rules ' + pcap_path + ' > ./result'
    os.system(cmd)


def upload_pcap_hit_rule(request):
    """
    :describe:  上传待检测pcap
    :param:     http请求
    :return:    上传结果信息,pcap路径
    """
    return_str = ""
    myFile = request.FILES.get("myfile", None)

    if not myFile:
        return_str = "未选择文件!"
        return return_str, ""

    if not str(myFile).endswith('.pcap'):
        return_str = "文件格式错误"
        return return_str, ""

    destination = open(os.path.join('./', myFile.name), 'wb+')

    for chunk in myFile.chunks():
        destination.write(chunk)
    destination.close()

    pcap_path = './' + myFile.name
    return return_str, pcap_path
