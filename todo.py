def load_todos():
    """从文件加载待办事项"""
    try:
        with open("todos.txt", "r", encoding="utf-8") as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        return []

def save_todos(todos):
    """保存待办事项到文件"""
    with open("todos.txt", "w", encoding="utf-8") as f:
        for todo in todos:
            f.write(todo + "\n")

def add_todo(todo):
    """添加新的待办事项"""
    todos = load_todos()
    todos.append(f"[ ] {todo}")
    save_todos(todos)
    print(f"已添加：{todo}")

def show_todos():
    """显示所有待办事项"""
    todos = load_todos()
    if not todos:
        print("暂无待办事项！")
        return
    print("\n待办事项列表：")
    for i, todo in enumerate(todos, 1):
        print(f"{i}. {todo}")
    print()

def complete_todo(index):
    """标记待办事项为已完成"""
    todos = load_todos()
    if 1 <= index <= len(todos):
        if todos[index-1].startswith("[ ]"):
            todos[index-1] = todos[index-1].replace("[ ]", "[x]")
            save_todos(todos)
            print(f"已完成：{todos[index-1][4:]}")
        else:
            print("该事项已完成！")
    else:
        print("序号无效！")

def delete_todo(index):
    """删除待办事项"""
    todos = load_todos()
    if 1 <= index <= len(todos):
        deleted = todos.pop(index-1)
        save_todos(todos)
        print(f"已删除：{deleted[4:]}")
    else:
        print("序号无效！")

def main():
    """主函数：显示菜单并处理用户输入"""
    while True:
        print("="*20)
        print("  待办事项管理器")
        print("1. 添加待办事项")
        print("2. 查看所有事项")
        print("3. 标记事项为完成")
        print("4. 删除事项")
        print("5. 退出")
        print("="*20)
        
        choice = input("请选择操作（1-5）：")
        if choice == "1":
            todo = input("请输入待办事项：")
            add_todo(todo)
        elif choice == "2":
            show_todos()
        elif choice == "3":
            index = int(input("请输入要标记的事项序号："))
            complete_todo(index)
        elif choice == "4":
            index = int(input("请输入要删除的事项序号："))
            delete_todo(index)
        elif choice == "5":
            print("再见！")
            break
        else:
            print("请输入正确的数字（1-5）！")

if __name__ == "__main__":
    main()
