import os
import random
import shutil


def modify_and_move_files(original_dir, target_dir):
    # 폴더가 없다면 생성
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    if not os.path.exists(target2_dir):
        os.makedirs(target2_dir)

    for filename in os.listdir(original_dir):
        if filename.endswith(".mdx"):
            new_filename = os.path.join(target_dir, filename)
            with open(os.path.join(original_dir, filename), "r", encoding="utf-8") as f:
                lines = f.readlines()
                with open(new_filename, "w", encoding="utf-8") as new_f:
                    # 첫 5줄은 그대로 작성
                    for i in range(5):
                        new_f.write(lines[i])
                    # 나머지 줄은 처리
                    for line in lines[5:]:
                        # '.'로 분할하고, 각 문장에 줄바꿈을 추가하여 다시 합침
                        if not line.startswith("#"):
                            sentences = line.split(". ")
                            new_line = ". \n".join(sentences)
                            new_f.write(new_line)
                        else:
                            new_f.write(line)
            # 원래 디렉토리의 파일 삭제
    for filename in os.listdir(target_dir):
        if filename.endswith(".mdx"):
            new_filename = os.path.join(target2_dir, filename)
            with open(os.path.join(target_dir, filename), "r", encoding="utf-8") as f:
                lines = f.readlines()
                with open(new_filename, "w", encoding="utf-8") as new_f:
                    # 첫 5줄은 그대로 작성
                    for i in range(5):
                        new_f.write(lines[i])
                    # 나머지 줄은 처리
                    for line in lines[5:]:
                        line = line.replace("요:", "요").replace("다:", "다")
                        # '.'로 분할하고, 각 문장에 줄바꿈을 추가하여 다시 합침
                        if line.startswith("#"):
                            new_f.write(line)
                        elif line.strip() == "":
                            new_f.write(line)
                        else:
                            words = line.split()
                            if len(words) > 2:
                                rand_word = random.choice(words[1:])
                                if random.choice([True, False]):
                                    line = line.replace(rand_word, f"**{rand_word}**")
                                else:
                                    line = line.replace(rand_word, f"_{rand_word}_")
                            new_f.write(line)

# 현재 스크립트의 위치를 찾음
current_script_path = os.path.dirname(os.path.abspath(__file__))

# 현재 스크립트의 위치를 기준으로 original_dir 경로를 설정
original_dir = os.path.join(current_script_path, 'posts')
target_dir = os.path.join(current_script_path, 'zz')
target2_dir = os.path.join(current_script_path, 'zz2')

modify_and_move_files(original_dir, target_dir)
