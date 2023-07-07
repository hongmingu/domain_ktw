import os
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
                        # '.'로 분할하고, 각 문장에 줄바꿈을 추가하여 다시 합침
                        if line.startswith("#"):
                            new_f.write(line)
                        elif line.strip() == "":
                            new_f.write(line)
                        else:
                            new_line = "-" + line
                            new_f.write(new_line)


original_dir = "/Users/moyoon/development/githubpage/domain_ktw/posts"
target_dir = "/Users/moyoon/development/githubpage/domain_ktw/zz"
target2_dir = "/Users/moyoon/development/githubpage/domain_ktw/zz2"

modify_and_move_files(original_dir, target_dir)
