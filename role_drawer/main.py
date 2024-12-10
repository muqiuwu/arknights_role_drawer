import tkinter as tk
from tkinter import ttk, messagebox, filedialog, simpledialog
import random
import json
import csv
import os
from datetime import datetime
import sys

# 数据文件路径
DATA_FILE = 'data.json'

# 默认数据
default_data = {
    "game_mode_characters": {
        "萨卡兹的无终奇语": {
            "strong": [
                "维什戴尔", "阿斯卡纶", "逻各斯", "令", "阿", "伊芙利特", "瑕光", "莫斯提马", "林", "艾雅法拉",
                "塑心", "灵知", "玛恩纳", "归溟幽灵鲨", "塞雷娅", "夜莺", "耀骑士临光", "假日威龙陈", "莱伊",
                "温蒂", "歌蕾蒂娅", "铃兰", "麒麟R夜刀", "艾拉", "缄默德克萨斯", "焰影苇草", "锏", "黍",
                "史尔特尔", "风笛", "琴柳", "刻俄柏", "伊内丝"
            ],
            "normal": [
                "荒芜拉普兰德", "引星棘刺", "忍冬", "佩佩", "维娜·维多利亚", "玛露西尔", "魔王", "乌尔比安",
                "娜仁图亚", "妮芙", "澄闪", "鸿雪", "提丰", "煌", "重岳", "圣约送葬人", "赫德雷", "缪尔赛思",
                "多萝西", "黑键", "山", "斥罪", "星熊", "凯尔希", "泥岩", "号角", "傀影", "银灰", "百炼嘉维尔",
                "仇白", "左乐", "白铁", "纯烬艾雅法拉", "浊心斯卡蒂", "麦哲伦", "年", "涤火杰西卡"
            ],
            "weak": [
                "弑君者", "伺夜", "W", "远牙", "推进之王", "焰尾", "帕拉斯", "赫拉格", "止颂", "棘刺", "异客",
                "流明", "水月", "菲亚梅塔", "夕", "空弦", "迷迭香", "能天使", "老鲤", "琳琅诗怀雅", "卡涅利安",
                "艾丽妮", "陈", "斯卡蒂", "嵯峨", "森蚺", "淬羽赫默", "安洁莉娜", "早露", "薇薇安娜", "灰烬",
                "霍尔海雅", "闪灵", "黑"
            ]
        },
        "探索者的银淞止境": {
            "strong": [
                "维什戴尔", "阿斯卡纶", "逻各斯", "令", "阿", "伊芙利特", "瑕光", "莫斯提马", "林", "艾雅法拉",
                "塑心", "灵知", "玛恩纳", "归溟幽灵鲨", "塞雷娅", "夜莺", "耀骑士临光", "假日威龙陈", "莱伊",
                "温蒂", "歌蕾蒂娅", "铃兰", "麒麟R夜刀", "艾拉", "缄默德克萨斯", "焰影苇草", "锏", "黍",
                "史尔特尔", "风笛", "琴柳", "刻俄柏", "伊内丝"
            ],
            "normal": [
                "荒芜拉普兰德", "引星棘刺", "忍冬", "佩佩", "维娜·维多利亚", "玛露西尔", "魔王", "乌尔比安",
                "娜仁图亚", "妮芙", "澄闪", "鸿雪", "提丰", "煌", "重岳", "圣约送葬人", "赫德雷", "缪尔赛思",
                "多萝西", "黑键", "山", "斥罪", "星熊", "凯尔希", "泥岩", "号角", "傀影", "银灰", "百炼嘉维尔",
                "仇白", "左乐", "白铁", "纯烬艾雅法拉", "浊心斯卡蒂", "麦哲伦", "年", "涤火杰西卡"
            ],
            "weak": [
                "弑君者", "伺夜", "W", "远牙", "推进之王", "焰尾", "帕拉斯", "赫拉格", "止颂", "棘刺", "异客",
                "流明", "水月", "菲亚梅塔", "夕", "空弦", "迷迭香", "能天使", "老鲤", "琳琅诗怀雅", "卡涅利安",
                "艾丽妮", "陈", "斯卡蒂", "嵯峨", "森蚺", "淬羽赫默", "安洁莉娜", "早露", "薇薇安娜", "灰烬",
                "霍尔海雅", "闪灵", "黑"
            ]
        },
        "水月与深蓝之树": {
            "strong": [
                "维什戴尔", "阿斯卡纶", "逻各斯", "令", "阿", "伊芙利特", "瑕光", "莫斯提马", "林", "艾雅法拉",
                "塑心", "灵知", "玛恩纳", "归溟幽灵鲨", "塞雷娅", "夜莺", "耀骑士临光", "假日威龙陈", "莱伊",
                "温蒂", "歌蕾蒂娅", "铃兰", "麒麟R夜刀", "艾拉", "缄默德克萨斯", "焰影苇草", "锏", "黍",
                "史尔特尔", "风笛", "琴柳", "刻俄柏", "伊内丝"
            ],
            "normal": [
                "荒芜拉普兰德", "引星棘刺", "忍冬", "佩佩", "维娜·维多利亚", "玛露西尔", "魔王", "乌尔比安",
                "娜仁图亚", "妮芙", "澄闪", "鸿雪", "提丰", "煌", "重岳", "圣约送葬人", "赫德雷", "缪尔赛思",
                "多萝西", "黑键", "山", "斥罪", "星熊", "凯尔希", "泥岩", "号角", "傀影", "银灰", "百炼嘉维尔",
                "仇白", "左乐", "白铁", "纯烬艾雅法拉", "浊心斯卡蒂", "麦哲伦", "年", "涤火杰西卡"
            ],
            "weak": [
                "弑君者", "伺夜", "W", "远牙", "推进之王", "焰尾", "帕拉斯", "赫拉格", "止颂", "棘刺", "异客",
                "流明", "水月", "菲亚梅塔", "夕", "空弦", "迷迭香", "能天使", "老鲤", "琳琅诗怀雅", "卡涅利安",
                "艾丽妮", "陈", "斯卡蒂", "嵯峨", "森蚺", "淬羽赫默", "安洁莉娜", "早露", "薇薇安娜", "灰烬",
                "霍尔海雅", "闪灵", "黑"
            ]
        },
        "傀影与猩红孤钻": {
            "strong": [
                "维什戴尔", "阿斯卡纶", "逻各斯", "令", "阿", "伊芙利特", "瑕光", "莫斯提马", "林", "艾雅法拉",
                "塑心", "灵知", "玛恩纳", "归溟幽灵鲨", "塞雷娅", "夜莺", "耀骑士临光", "假日威龙陈", "莱伊",
                "温蒂", "歌蕾蒂娅", "铃兰", "麒麟R夜刀", "艾拉", "缄默德克萨斯", "焰影苇草", "锏", "黍",
                "史尔特尔", "风笛", "琴柳", "刻俄柏", "伊内丝"
            ],
            "normal": [
                "荒芜拉普兰德", "引星棘刺", "忍冬", "佩佩", "维娜·维多利亚", "玛露西尔", "魔王", "乌尔比安",
                "娜仁图亚", "妮芙", "澄闪", "鸿雪", "提丰", "煌", "重岳", "圣约送葬人", "赫德雷", "缪尔赛思",
                "多萝西", "黑键", "山", "斥罪", "星熊", "凯尔希", "泥岩", "号角", "傀影", "银灰", "百炼嘉维尔",
                "仇白", "左乐", "白铁", "纯烬艾雅法拉", "浊心斯卡蒂", "麦哲伦", "年", "涤火杰西卡"
            ],
            "weak": [
                "弑君者", "伺夜", "W", "远牙", "推进之王", "焰尾", "帕拉斯", "赫拉格", "止颂", "棘刺", "异客",
                "流明", "水月", "菲亚梅塔", "夕", "空弦", "迷迭香", "能天使", "老鲤", "琳琅诗怀雅", "卡涅利安",
                "艾丽妮", "陈", "斯卡蒂", "嵯峨", "森蚺", "淬羽赫默", "安洁莉娜", "早露", "薇薇安娜", "灰烬",
                "霍尔海雅", "闪灵", "黑"
            ]
        }
    },
    "levels": {
        "傀影与猩红孤钻": ["古堡观光", "正式调查", "直面灾厄"],
        "水月与深蓝之树": [str(i) for i in range(1, 16)],
        "探索者的银淞止境": [str(i) for i in range(1, 16)],
        "萨卡兹的无终奇语": [str(i) for i in range(1, 16)]
    },
    "teams": {
        "傀影与猩红孤钻": ["指挥分队", "集群分队", "后勤分队", "矛头分队", "突击战术分队", "堡垒战术分队",
                           "远程战术分队", "破坏战术分队", "研究分队", "高规格分队"],
        "水月与深蓝之树": ["新胜于物分队", "物尽其用分队", "以人为本分队", "指挥分队", "集群分队",
                           "后勤分队", "矛头分队", "突击战术分队", "堡垒战术分队", "远程战术分队",
                           "破坏战术分队", "研究分队", "高规格分队"],
        "探索者的银淞止境": ["永恒狩猎分队", "生活至上分队", "科学主义分队", "特训分队", "指挥分队",
                             "集群分队", "后勤分队", "矛头分队", "突击战术分队", "堡垒战术分队",
                             "远程战术分队", "破坏战术分队", "高规格分队"],
        "萨卡兹的无终奇语": ["拟态学者分队", "异想天开分队", "点刺成锭分队", "因地制宜分队",
                             "魂灵护送分队", "博闻广记分队", "蓝图测绘分队", "指挥分队", "集群分队",
                             "后勤分队", "矛头分队", "突击战术分队", "堡垒战术分队", "远程战术分队",
                             "破坏战术分队", "研究分队", "高规格分队"]
    }
}


def resource_path(relative_path):
    """获取资源文件的绝对路径，兼容打包后的环境。"""
    try:
        # PyInstaller创建临时文件夹并将路径存储在_MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# 数据文件路径
DATA_FILE = resource_path('data.json')

def set_app_icon():
    """设置应用程序图标。"""
    try:
        # 假设图标文件名为 'icon.ico'，放在当前目录下
        icon_path = resource_path('icon.ico')
        if os.path.exists(icon_path):
            root.iconbitmap(icon_path)
    except Exception as e:
        print(f"设置图标时出错: {e}")


def load_data():
    """加载数据，如果数据文件不存在则创建并使用默认数据。"""
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(default_data, f, ensure_ascii=False, indent=4)
        return default_data
    else:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)


def save_data(data):
    """将数据保存到数据文件中。"""
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


# 加载数据
data = load_data()
game_mode_characters = data["game_mode_characters"]
levels = data["levels"]
teams = data["teams"]


def refresh_gui_data():
    """刷新GUI中使用的数据，如下拉菜单等。"""
    # 更新游戏模式菜单
    menu = mode_menu["menu"]
    menu.delete(0, "end")
    for mode in game_modes:
        menu.add_command(label=mode, command=lambda value=mode: mode_var.set(value))

    # 更新关卡和分队
    update_levels_and_teams()


def update_levels_and_teams():
    """根据当前选择的游戏模式，更新关卡和分队的下拉菜单。"""
    current_mode = mode_var.get()

    # 更新关卡
    level_menu['menu'].delete(0, 'end')
    for level in levels.get(current_mode, []):
        level_menu['menu'].add_command(label=level, command=lambda value=level: level_var.set(value))
    if levels.get(current_mode):
        level_var.set(levels[current_mode][0])
    else:
        level_var.set("")

    # 更新分队
    team_menu['menu'].delete(0, 'end')
    for team in teams.get(current_mode, []):
        team_menu['menu'].add_command(label=team, command=lambda value=team: team_var.set(value))
    if teams.get(current_mode):
        team_var.set(teams[current_mode][0])
    else:
        team_var.set("")


def manage_data():
    """打开管理数据的窗口。"""
    ManageWindow(root, data)


class ManageWindow(tk.Toplevel):
    def __init__(self, master, data):
        super().__init__(master)
        self.title("🔧 管理数据")
        self.geometry("600x400")
        self.data = data
        self.create_widgets()

    def create_widgets(self):
        """创建管理窗口的组件。"""
        # 创建标签和选项卡
        tab_control = ttk.Notebook(self)

        self.mode_tab = ttk.Frame(tab_control)
        self.level_tab = ttk.Frame(tab_control)
        self.team_tab = ttk.Frame(tab_control)
        self.character_tab = ttk.Frame(tab_control)

        tab_control.add(self.mode_tab, text='游戏模式')
        tab_control.add(self.level_tab, text='关卡')
        tab_control.add(self.team_tab, text='队伍')
        tab_control.add(self.character_tab, text='角色')

        tab_control.pack(expand=1, fill='both')

        self.create_mode_tab()
        self.create_level_tab()
        self.create_team_tab()
        self.create_character_tab()

    def create_mode_tab(self):
        """创建游戏模式管理界面。"""
        frame = self.mode_tab
        # 列表框显示游戏模式
        self.mode_listbox = tk.Listbox(frame)
        self.mode_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.update_mode_listbox()

        # 右侧按钮
        btn_frame = ttk.Frame(frame)
        btn_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=10, pady=10)

        add_btn = ttk.Button(btn_frame, text="添加模式", command=self.add_mode)
        add_btn.pack(fill=tk.X, pady=5)

        delete_btn = ttk.Button(btn_frame, text="删除模式", command=self.delete_mode)
        delete_btn.pack(fill=tk.X, pady=5)

        rename_btn = ttk.Button(btn_frame, text="重命名模式", command=self.rename_mode)
        rename_btn.pack(fill=tk.X, pady=5)

    def update_mode_listbox(self):
        """更新游戏模式列表框。"""
        self.mode_listbox.delete(0, tk.END)
        for mode in self.data["game_mode_characters"].keys():
            self.mode_listbox.insert(tk.END, mode)

    def add_mode(self):
        """添加新的游戏模式。"""
        new_mode = simpledialog.askstring("添加模式", "请输入新的游戏模式名称：")
        if new_mode:
            if new_mode in self.data["game_mode_characters"]:
                messagebox.showerror("错误", "该模式已存在。")
                return
            self.data["game_mode_characters"][new_mode] = {"strong": [], "normal": [], "weak": []}
            self.data["levels"][new_mode] = []
            self.data["teams"][new_mode] = []
            save_data(self.data)
            self.update_mode_listbox()
            refresh_gui_data()

    def delete_mode(self):
        """删除选中的游戏模式。"""
        selected = self.mode_listbox.curselection()
        if not selected:
            messagebox.showwarning("警告", "请选择一个模式进行删除。")
            return
        mode = self.mode_listbox.get(selected[0])
        if messagebox.askyesno("确认删除", f"确定要删除模式 '{mode}' 吗？"):
            del self.data["game_mode_characters"][mode]
            del self.data["levels"][mode]
            del self.data["teams"][mode]
            save_data(self.data)
            self.update_mode_listbox()
            refresh_gui_data()

    def rename_mode(self):
        """重命名选中的游戏模式。"""
        selected = self.mode_listbox.curselection()
        if not selected:
            messagebox.showwarning("警告", "请选择一个模式进行重命名。")
            return
        old_mode = self.mode_listbox.get(selected[0])
        new_mode = simpledialog.askstring("重命名模式", f"请输入模式 '{old_mode}' 的新名称：")
        if new_mode:
            if new_mode in self.data["game_mode_characters"]:
                messagebox.showerror("错误", "该模式已存在。")
                return
            self.data["game_mode_characters"][new_mode] = self.data["game_mode_characters"].pop(old_mode)
            self.data["levels"][new_mode] = self.data["levels"].pop(old_mode)
            self.data["teams"][new_mode] = self.data["teams"].pop(old_mode)
            save_data(self.data)
            self.update_mode_listbox()
            refresh_gui_data()

    def create_level_tab(self):
        """创建关卡管理界面。"""
        frame = self.level_tab
        # 选择游戏模式
        mode_label = ttk.Label(frame, text="选择游戏模式:")
        mode_label.pack(pady=5)

        self.level_mode_var = tk.StringVar()
        self.level_mode_menu = ttk.OptionMenu(frame, self.level_mode_var, None,
                                              *self.data["game_mode_characters"].keys(),
                                              command=self.update_level_listbox)
        self.level_mode_menu.pack(pady=5)

        # 列表框显示关卡
        self.level_listbox = tk.Listbox(frame)
        self.level_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        # 右侧按钮
        btn_frame = ttk.Frame(frame)
        btn_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=10, pady=10)

        add_btn = ttk.Button(btn_frame, text="添加关卡", command=self.add_level)
        add_btn.pack(fill=tk.X, pady=5)

        delete_btn = ttk.Button(btn_frame, text="删除关卡", command=self.delete_level)
        delete_btn.pack(fill=tk.X, pady=5)

        rename_btn = ttk.Button(btn_frame, text="重命名关卡", command=self.rename_level)
        rename_btn.pack(fill=tk.X, pady=5)

    def update_level_listbox(self, *args):
        """更新关卡列表框。"""
        mode = self.level_mode_var.get()
        if not mode:
            self.level_listbox.delete(0, tk.END)
            return
        self.level_listbox.delete(0, tk.END)
        for level in self.data["levels"].get(mode, []):
            self.level_listbox.insert(tk.END, level)

    def add_level(self):
        """添加新的关卡。"""
        mode = self.level_mode_var.get()
        if not mode:
            messagebox.showwarning("警告", "请选择一个游戏模式。")
            return
        new_level = simpledialog.askstring("添加关卡", "请输入新的关卡名称：")
        if new_level:
            if new_level in self.data["levels"][mode]:
                messagebox.showerror("错误", "该关卡已存在。")
                return
            self.data["levels"][mode].append(new_level)
            save_data(self.data)
            self.update_level_listbox()

    def delete_level(self):
        """删除选中的关卡。"""
        mode = self.level_mode_var.get()
        if not mode:
            messagebox.showwarning("警告", "请选择一个游戏模式。")
            return
        selected = self.level_listbox.curselection()
        if not selected:
            messagebox.showwarning("警告", "请选择一个关卡进行删除。")
            return
        level = self.level_listbox.get(selected[0])
        if messagebox.askyesno("确认删除", f"确定要删除关卡 '{level}' 吗？"):
            self.data["levels"][mode].remove(level)
            save_data(self.data)
            self.update_level_listbox()

    def rename_level(self):
        """重命名选中的关卡。"""
        mode = self.level_mode_var.get()
        if not mode:
            messagebox.showwarning("警告", "请选择一个游戏模式。")
            return
        selected = self.level_listbox.curselection()
        if not selected:
            messagebox.showwarning("警告", "请选择一个关卡进行重命名。")
            return
        old_level = self.level_listbox.get(selected[0])
        new_level = simpledialog.askstring("重命名关卡", f"请输入关卡 '{old_level}' 的新名称：")
        if new_level:
            if new_level in self.data["levels"][mode]:
                messagebox.showerror("错误", "该关卡已存在。")
                return
            index = self.data["levels"][mode].index(old_level)
            self.data["levels"][mode][index] = new_level
            save_data(self.data)
            self.update_level_listbox()

    def create_team_tab(self):
        """创建队伍管理界面。"""
        frame = self.team_tab
        # 选择游戏模式
        mode_label = ttk.Label(frame, text="选择游戏模式:")
        mode_label.pack(pady=5)

        self.team_mode_var = tk.StringVar()
        self.team_mode_menu = ttk.OptionMenu(frame, self.team_mode_var, None, *self.data["game_mode_characters"].keys(),
                                             command=self.update_team_listbox)
        self.team_mode_menu.pack(pady=5)

        # 列表框显示队伍
        self.team_listbox = tk.Listbox(frame)
        self.team_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        # 右侧按钮
        btn_frame = ttk.Frame(frame)
        btn_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=10, pady=10)

        add_btn = ttk.Button(btn_frame, text="添加队伍", command=self.add_team)
        add_btn.pack(fill=tk.X, pady=5)

        delete_btn = ttk.Button(btn_frame, text="删除队伍", command=self.delete_team)
        delete_btn.pack(fill=tk.X, pady=5)

        rename_btn = ttk.Button(btn_frame, text="重命名队伍", command=self.rename_team)
        rename_btn.pack(fill=tk.X, pady=5)

    def update_team_listbox(self, *args):
        """更新队伍列表框。"""
        mode = self.team_mode_var.get()
        if not mode:
            self.team_listbox.delete(0, tk.END)
            return
        self.team_listbox.delete(0, tk.END)
        for team in self.data["teams"].get(mode, []):
            self.team_listbox.insert(tk.END, team)

    def add_team(self):
        """添加新的队伍。"""
        mode = self.team_mode_var.get()
        if not mode:
            messagebox.showwarning("警告", "请选择一个游戏模式。")
            return
        new_team = simpledialog.askstring("添加队伍", "请输入新的队伍名称：")
        if new_team:
            if new_team in self.data["teams"][mode]:
                messagebox.showerror("错误", "该队伍已存在。")
                return
            self.data["teams"][mode].append(new_team)
            save_data(self.data)
            self.update_team_listbox()

    def delete_team(self):
        """删除选中的队伍。"""
        mode = self.team_mode_var.get()
        if not mode:
            messagebox.showwarning("警告", "请选择一个游戏模式。")
            return
        selected = self.team_listbox.curselection()
        if not selected:
            messagebox.showwarning("警告", "请选择一个队伍进行删除。")
            return
        team = self.team_listbox.get(selected[0])
        if messagebox.askyesno("确认删除", f"确定要删除队伍 '{team}' 吗？"):
            self.data["teams"][mode].remove(team)
            save_data(self.data)
            self.update_team_listbox()

    def rename_team(self):
        """重命名选中的队伍。"""
        mode = self.team_mode_var.get()
        if not mode:
            messagebox.showwarning("警告", "请选择一个游戏模式。")
            return
        selected = self.team_listbox.curselection()
        if not selected:
            messagebox.showwarning("警告", "请选择一个队伍进行重命名。")
            return
        old_team = self.team_listbox.get(selected[0])
        new_team = simpledialog.askstring("重命名队伍", f"请输入队伍 '{old_team}' 的新名称：")
        if new_team:
            if new_team in self.data["teams"][mode]:
                messagebox.showerror("错误", "该队伍已存在。")
                return
            index = self.data["teams"][mode].index(old_team)
            self.data["teams"][mode][index] = new_team
            save_data(self.data)
            self.update_team_listbox()

    def create_character_tab(self):
        """创建角色管理界面。"""
        frame = self.character_tab
        # 选择游戏模式和强度
        top_frame = ttk.Frame(frame)
        top_frame.pack(pady=5)

        mode_label = ttk.Label(top_frame, text="游戏模式:")
        mode_label.grid(row=0, column=0, padx=5, pady=5)

        self.char_mode_var = tk.StringVar()
        self.char_mode_menu = ttk.OptionMenu(top_frame, self.char_mode_var, None,
                                             *self.data["game_mode_characters"].keys(),
                                             command=self.update_character_listbox)
        self.char_mode_menu.grid(row=0, column=1, padx=5, pady=5)

        strength_label = ttk.Label(top_frame, text="强度:")
        strength_label.grid(row=0, column=2, padx=5, pady=5)

        self.char_strength_var = tk.StringVar()
        self.char_strength_menu = ttk.OptionMenu(top_frame, self.char_strength_var, "strong", "strong", "normal",
                                                 "weak", command=self.update_character_listbox)
        self.char_strength_menu.grid(row=0, column=3, padx=5, pady=5)

        # 列表框显示角色
        self.character_listbox = tk.Listbox(frame)
        self.character_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        # 右侧按钮
        btn_frame = ttk.Frame(frame)
        btn_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=10, pady=10)

        add_btn = ttk.Button(btn_frame, text="添加角色", command=self.add_character)
        add_btn.pack(fill=tk.X, pady=5)

        delete_btn = ttk.Button(btn_frame, text="删除角色", command=self.delete_character)
        delete_btn.pack(fill=tk.X, pady=5)

    def update_character_listbox(self, *args):
        """更新角色列表框。"""
        mode = self.char_mode_var.get()
        strength = self.char_strength_var.get()
        if not mode or not strength:
            self.character_listbox.delete(0, tk.END)
            return
        self.character_listbox.delete(0, tk.END)
        for char in self.data["game_mode_characters"].get(mode, {}).get(strength, []):
            self.character_listbox.insert(tk.END, char)

    def add_character(self):
        """添加新的角色。"""
        mode = self.char_mode_var.get()
        strength = self.char_strength_var.get()
        if not mode or not strength:
            messagebox.showwarning("警告", "请选择游戏模式和强度。")
            return
        new_char = simpledialog.askstring("添加角色", f"请输入要添加到 '{strength}' 的新角色名称：")
        if new_char:
            if new_char in self.data["game_mode_characters"][mode][strength]:
                messagebox.showerror("错误", "该角色已存在。")
                return
            self.data["game_mode_characters"][mode][strength].append(new_char)
            save_data(self.data)
            self.update_character_listbox()

    def delete_character(self):
        """删除选中的角色。"""
        mode = self.char_mode_var.get()
        strength = self.char_strength_var.get()
        if not mode or not strength:
            messagebox.showwarning("警告", "请选择游戏模式和强度。")
            return
        selected = self.character_listbox.curselection()
        if not selected:
            messagebox.showwarning("警告", "请选择一个角色进行删除。")
            return
        char = self.character_listbox.get(selected[0])
        if messagebox.askyesno("确认删除", f"确定要删除角色 '{char}' 吗？"):
            self.data["game_mode_characters"][mode][strength].remove(char)
            save_data(self.data)
            self.update_character_listbox()


def draw_characters():
    """启动角色抽取动画，并在完成后显示结果。"""
    try:
        # 获取用户自定义的角色数量
        num_strong = int(strong_spinbox.get())
        num_normal = int(normal_spinbox.get())
        num_weak = int(weak_spinbox.get())

        # 获取当前游戏模式的角色池
        current_mode = mode_var.get()
        current_characters = game_mode_characters.get(current_mode, {})
        strong_characters_pool = current_characters.get("strong", [])
        normal_characters_pool = current_characters.get("normal", [])
        weak_characters_pool = current_characters.get("weak", [])

        # 验证选择数量是否合理
        if num_strong > len(strong_characters_pool):
            raise ValueError(f"超大杯最多可选 {len(strong_characters_pool)} 个角色。")
        if num_normal > len(normal_characters_pool):
            raise ValueError(f"大杯最多可选 {len(normal_characters_pool)} 个角色。")
        if num_weak > len(weak_characters_pool):
            raise ValueError(f"中杯最多可选 {len(weak_characters_pool)} 个角色。")
    except ValueError as ve:
        messagebox.showerror("输入错误", str(ve))
        return

    # 启动动画
    draw_button.config(state='disabled')
    save_button.config(state='disabled')
    copy_button.config(state='disabled')
    progress_bar.start()
    result_text_widget.config(state='normal')
    result_text_widget.delete(1.0, tk.END)
    result_text_widget.insert(tk.END, "🎲 抽取中，请稍候...\n")
    result_text_widget.config(state='disabled')
    root.update()

    # 模拟动画延迟（例如2秒），然后开始动态显示结果
    root.after(2000, lambda: start_dynamic_display(num_strong, num_normal, num_weak, strong_characters_pool,
                                                   normal_characters_pool, weak_characters_pool))


def start_dynamic_display(num_strong, num_normal, num_weak, strong_pool, normal_pool, weak_pool):
    """开始动态显示抽取结果。"""
    global selected_strong, selected_normal, selected_weak, selected_level, selected_team, display_index, display_texts

    # 从每种强度的角色中抽取指定数量
    selected_strong = random.sample(strong_pool, num_strong)
    selected_normal = random.sample(normal_pool, num_normal)
    selected_weak = random.sample(weak_pool, num_weak)

    # 随机选择关卡
    selected_level = random.choice(levels[mode_var.get()]) if levels.get(mode_var.get()) else "无关卡"
    # 随机选择分队
    selected_team = random.choice(teams[mode_var.get()]) if teams.get(mode_var.get()) else "无分队"

    # 生成结果文本
    result_text = (
        f"游戏模式: {mode_var.get()}\n\n"
        f"难度: {selected_level}\n\n"
        f"分队: {selected_team}\n\n"
        f"超大杯 ({num_strong}):\n\n {'    '.join(selected_strong)}\n\n"
        f"大杯 ({num_normal}):\n\n {'    '.join(selected_normal)}\n\n"
        f"中杯 ({num_weak}):\n\n {'    '.join(selected_weak)}"
    )

    # 分割文本为逐行显示
    display_texts = result_text.split('\n')
    display_index = 0
    result_text_widget.config(state='normal')
    result_text_widget.delete(1.0, tk.END)
    result_text_widget.config(state='disabled')
    animate_text(display_texts, display_index)


def animate_text(display_texts, display_index, char_index=0):
    """逐字符显示文本，并添加颜色变化效果。"""
    if display_index < len(display_texts):
        line = display_texts[display_index]
        if char_index < len(line):
            result_text_widget.config(state='normal')
            char = line[char_index]
            # 添加单个字符
            result_text_widget.insert(tk.END, char)
            # 为字符添加随机颜色
            result_text_widget.tag_add(f"char{display_index}_{char_index}", f"{display_index + 1}.{char_index}")
            result_text_widget.tag_config(f"char{display_index}_{char_index}")#, foreground=random_color()#改变颜色代码
            result_text_widget.config(state='disabled')
            display_index_new = display_index
            char_index_new = char_index + 1
            root.after(15, lambda: animate_text(display_texts, display_index_new, char_index_new))
        else:
            # 换行
            result_text_widget.config(state='normal')
            result_text_widget.insert(tk.END, '\n')
            result_text_widget.config(state='disabled')
            display_index_new = display_index + 1
            char_index_new = 0
            root.after(30, lambda: animate_text(display_texts, display_index_new, char_index_new))
    else:
        # 动画完成，停止进度条，恢复按钮状态
        progress_bar.stop()
        draw_button.config(state='normal')
        save_button.config(state='normal')
        copy_button.config(state='normal')


def random_color():
    """生成随机颜色代码。"""
    return f"#{random.randint(0, 0xFFFFFF):06x}"


def copy_to_clipboard():
    """将结果文本复制到剪贴板。"""
    result_text = result_text_widget.get("1.0", tk.END).strip()
    if result_text:
        root.clipboard_clear()
        root.clipboard_append(result_text)
        root.update()  # 确保剪贴板内容被更新
        # 显示提示
        copy_label.config(text="✅ 结果已复制到剪贴板！")
        root.after(2000, lambda: copy_label.config(text=""))


def save_results():
    """保存抽取结果为文本、JSON或CSV文件。"""
    result_text = result_text_widget.get("1.0", tk.END).strip()
    if not result_text:
        messagebox.showwarning("保存结果", "没有结果可以保存。")
        return

    # 自动生成默认文件名
    default_filename = datetime.now().strftime("抽取结果_%Y%m%d_%H%M%S")

    file_types = [
        ("Text Files", "*.txt"),
        ("JSON Files", "*.json"),
        ("CSV Files", "*.csv")
    ]
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", initialfile=default_filename,
                                             filetypes=file_types)
    if not file_path:
        return  # 用户取消保存

    try:
        if file_path.endswith('.txt'):
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(result_text)
        elif file_path.endswith('.json'):
            # 解析结果文本为字典
            lines = result_text.split('\n')
            data_dict = {}
            current_key = None
            for line in lines:
                if ": " in line:
                    key, value = line.split(": ", 1)
                    current_key = key.strip()
                    data_dict[current_key] = value.strip()
                elif current_key and line.strip():
                    data_dict[current_key] += f", {line.strip()}"
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data_dict, f, ensure_ascii=False, indent=4)
        elif file_path.endswith('.csv'):
            # 解析结果文本为列表
            lines = result_text.split('\n')
            with open(file_path, 'w', encoding='utf-8', newline='') as f:
                writer = csv.writer(f)
                for line in lines:
                    if ": " in line:
                        writer.writerow(line.split(": ", 1))
                    else:
                        writer.writerow([line])
        messagebox.showinfo("保存成功", f"结果已成功保存到 {file_path}")
    except Exception as e:
        messagebox.showerror("保存失败", f"保存结果时出错：{e}")


def set_app_icon():
    """设置应用程序图标。"""
    try:
        # 假设图标文件名为 'icon.ico'，放在当前目录下
        icon_path = os.path.join(os.path.dirname(__file__), 'icon.ico')
        if os.path.exists(icon_path):
            root.iconbitmap(icon_path)
    except Exception as e:
        print(f"设置图标时出错: {e}")


# 创建 GUI 窗口
root = tk.Tk()
root.title("🎲 角色抽取器")
root.geometry("700x1000")  # 调整窗口大小
root.resizable(True, True)  # 允许调整大小

# 设置应用程序图标
set_app_icon()

# 设置主题
style = ttk.Style(root)
style.theme_use('clam')  # 选择现代化主题

# 定义颜色
BACKGROUND_COLOR = "#2C3E50"
FRAME_COLOR = "#34495E"
BUTTON_COLOR = "#1ABC9C"
LABEL_COLOR = "#ECF0F1"
TEXT_COLOR = "#ECF0F1"

# 自定义样式
style.configure("MainFrame.TFrame", background=BACKGROUND_COLOR)
style.configure("TLabel", background=BACKGROUND_COLOR, foreground=LABEL_COLOR, font=("Helvetica", 12))
style.configure("Header.TLabel", background=BACKGROUND_COLOR, foreground=LABEL_COLOR, font=("Helvetica", 18, "bold"))
style.configure("TButton", font=("Helvetica", 12, "bold"), foreground=BACKGROUND_COLOR, background=BUTTON_COLOR)
style.map("TButton",
          background=[('active', BUTTON_COLOR)],
          foreground=[('active', BACKGROUND_COLOR)])
style.configure("TSpinbox", font=("Helvetica", 12))

# 主框架
main_frame = ttk.Frame(root, padding="20 20 20 20", style="MainFrame.TFrame")
main_frame.pack(fill=tk.BOTH, expand=True)

# 添加说明标签
instructions_label = ttk.Label(
    main_frame, text="选择游戏模式、设置抽取数量并点击抽取角色",
    style="Header.TLabel", anchor="center", justify="center"
)
instructions_label.grid(row=0, column=0, columnspan=4, pady=(0, 20))

# 选择游戏模式
mode_label = ttk.Label(main_frame, text="选择游戏模式:")
mode_label.grid(row=1, column=0, sticky="w", pady=(10, 5))

mode_var = tk.StringVar(value=list(game_mode_characters.keys())[0])  # 默认选择第一个模式

mode_menu = ttk.OptionMenu(main_frame, mode_var, list(game_mode_characters.keys())[0],
                           *list(game_mode_characters.keys()), command=lambda _: update_levels_and_teams())
mode_menu.grid(row=1, column=1, columnspan=3, sticky="ew", pady=(10, 5))

# 配置列权重以实现响应式布局
main_frame.columnconfigure(0, weight=1)
main_frame.columnconfigure(1, weight=1)
main_frame.columnconfigure(2, weight=1)
main_frame.columnconfigure(3, weight=1)

# 自定义角色数量
# 超大杯
strong_label = ttk.Label(main_frame, text="💎 超大杯数量:")
strong_label.grid(row=2, column=0, sticky="w", pady=(10, 5))
strong_spinbox = ttk.Spinbox(main_frame, from_=1, to=10, width=5)
strong_spinbox.set(4)  # 默认值
strong_spinbox.grid(row=2, column=1, sticky="w", pady=(10, 5))

# 大杯
normal_label = ttk.Label(main_frame, text="🥇 大杯数量:")
normal_label.grid(row=3, column=0, sticky="w", pady=(10, 5))
normal_spinbox = ttk.Spinbox(main_frame, from_=1, to=10, width=5)
normal_spinbox.set(4)  # 默认值
normal_spinbox.grid(row=3, column=1, sticky="w", pady=(10, 5))

# 中杯
weak_label = ttk.Label(main_frame, text="🥉 中杯数量:")
weak_label.grid(row=4, column=0, sticky="w", pady=(10, 5))
weak_spinbox = ttk.Spinbox(main_frame, from_=1, to=10, width=5)
weak_spinbox.set(4)  # 默认值
weak_spinbox.grid(row=4, column=1, sticky="w", pady=(10, 5))

# 抽取按钮
draw_button = ttk.Button(main_frame, text="🎲 抽取角色", command=draw_characters)
draw_button.grid(row=5, column=0, columnspan=4, pady=(20, 10), sticky="ew")

# 进度条
progress_bar = ttk.Progressbar(main_frame, mode='indeterminate')
progress_bar.grid(row=6, column=0, columnspan=4, sticky="ew", pady=(0, 10))

# 分割线
separator = ttk.Separator(main_frame, orient='horizontal')
separator.grid(row=7, column=0, columnspan=4, sticky="ew", pady=10)

# 结果显示区域
result_frame = ttk.Frame(main_frame, style="MainFrame.TFrame")
result_frame.grid(row=8, column=0, columnspan=4, sticky="nsew")

# 配置行权重以让结果区域扩展
main_frame.rowconfigure(8, weight=1)
result_frame.columnconfigure(0, weight=1)
result_frame.rowconfigure(0, weight=1)

# 增加滚动条
result_text_widget = tk.Text(
    result_frame, wrap='word', font=("Helvetica", 12), bg="#34495E",
    fg=TEXT_COLOR, bd=0, highlightthickness=0
)
result_text_widget.grid(row=0, column=0, sticky="nsew")

scrollbar = ttk.Scrollbar(result_frame, orient="vertical", command=result_text_widget.yview)
scrollbar.grid(row=0, column=1, sticky="ns")

result_text_widget.configure(yscrollcommand=scrollbar.set, state='disabled')

# 美化滚动条
style.configure("Vertical.TScrollbar", background=BUTTON_COLOR, troughcolor=FRAME_COLOR)
scrollbar.configure(style="Vertical.TScrollbar")

# 添加背景色到结果文本
result_text_widget.configure(bg=FRAME_COLOR, fg=TEXT_COLOR, insertbackground=TEXT_COLOR)

# 添加“复制结果”按钮
copy_button = ttk.Button(main_frame, text="📋 复制结果", command=copy_to_clipboard)
copy_button.grid(row=9, column=0, columnspan=4, pady=(10, 5), sticky="ew")

# 添加“保存结果”按钮
save_button = ttk.Button(main_frame, text="💾 保存结果", command=save_results)
save_button.grid(row=10, column=0, columnspan=4, pady=(0, 10), sticky="ew")

# 添加“管理数据”按钮
manage_button = ttk.Button(main_frame, text="🔧 管理数据", command=manage_data)
manage_button.grid(row=11, column=0, columnspan=4, pady=(0, 10), sticky="ew")

# 添加复制结果后的提示标签
copy_label = ttk.Label(main_frame, text="", style="TLabel")
copy_label.grid(row=12, column=0, columnspan=4, pady=(0, 10))


def update_levels_and_teams():
    """根据当前选择的游戏模式，更新关卡和分队的下拉菜单。"""
    current_mode = mode_var.get()

    # 更新关卡
    level_menu['menu'].delete(0, 'end')
    for level in levels.get(current_mode, []):
        level_menu['menu'].add_command(label=level, command=lambda value=level: level_var.set(value))
    if levels.get(current_mode):
        level_var.set(levels[current_mode][0])
    else:
        level_var.set("")

    # 更新分队
    team_menu['menu'].delete(0, 'end')
    for team in teams.get(current_mode, []):
        team_menu['menu'].add_command(label=team, command=lambda value=team: team_var.set(value))
    if teams.get(current_mode):
        team_var.set(teams[current_mode][0])
    else:
        team_var.set("")


# 添加关卡和分队的下拉菜单（不可见，自动选择）
level_label = ttk.Label(main_frame, text="关卡:")
level_label.grid(row=12, column=0, sticky="w", pady=(0, 5), padx=20)
level_var = tk.StringVar()
level_menu = ttk.OptionMenu(main_frame, level_var, "")
level_menu.grid(row=12, column=1, columnspan=3, sticky="ew", pady=(0, 5), padx=20)

team_label = ttk.Label(main_frame, text="分队:")
team_label.grid(row=13, column=0, sticky="w", pady=(0, 5), padx=20)
team_var = tk.StringVar()
team_menu = ttk.OptionMenu(main_frame, team_var, "")
team_menu.grid(row=13, column=1, columnspan=3, sticky="ew", pady=(0, 5), padx=20)

# 初始化关卡和分队
update_levels_and_teams()

# 运行主循环
root.mainloop()
