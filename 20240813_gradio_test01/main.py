import gradio as gr
import json

# 전화번호부 초기화
phonebook_data = {
    0: {'Name': 'Kim', 'Phone': '45648733'},
    1: {'Name': 'Lee', 'Phone': '89376333'},
    2: {'Name': 'Park', 'Phone': '36457818'},
    3: {'Name': 'Chung', 'Phone': '76891234'},
    4: {'Name': 'Choi', 'Phone': '67451237'}
}

# 전화번호부 확인 함수
def check_phonebook(name):
    name = name.lower()
    for entry in phonebook_data.values():
        if entry['Name'].lower() == name:
            return f"{entry['Name']}의 번호는 {entry['Phone']}입니다."
    return f"{name}을(를) 찾을 수 없습니다."

# 전화번호부 추가 함수
def add_to_phonebook(name, phone):
    new_key = max(phonebook_data.keys(), default=-1) + 1
    phonebook_data[new_key] = {'Name': name, 'Phone': phone}
    return f"{name} 추가 완료"

# 전화번호부 삭제 함수
def delete_from_phonebook(name):
    name = name.lower()
    for key, entry in list(phonebook_data.items()):
        if entry['Name'].lower() == name:
            del phonebook_data[key]
            return f"{name} 삭제 완료"
    return f"{name}을(를) 찾을 수 없습니다."

# Gradio 인터페이스 생성
check_interface = gr.Interface(
    fn=check_phonebook,
    inputs=gr.Textbox(label="확인할 이름"),
    outputs="text",
    title="전화번호부 확인"
)

add_interface = gr.Interface(
    fn=add_to_phonebook,
    inputs=[gr.Textbox(label="추가할 이름"), gr.Textbox(label="추가할 번호")],
    outputs="text",
    title="전화번호부 추가"
)

delete_interface = gr.Interface(
    fn=delete_from_phonebook,
    inputs=gr.Textbox(label="삭제할 이름"),
    outputs="text",
    title="전화번호부 삭제"
)

# 인터페이스 실행
gr.TabbedInterface([check_interface, add_interface, delete_interface], ["확인", "추가", "삭제"]).launch()