"""
    https://taemham.github.io/posts/CodeTree_SantaFactory/
"""


class Box:
    # 연결리스트 노드 생성자에 id와 무게를 추가
    def __init__(self, box_id, weight):
        self.box_id = box_id
        self.weight = weight
        self.prev_box: Box = None
        self.next_box: Box = None

    # 노드의 앞과 뒤 주소를 넣어주는 메서드
    def set_prev(self, prev_box):
        self.prev_box = prev_box

    def set_next(self, next_box):
        self.next_box = next_box

    # 앞의 노드와의 연결을 끊는 메서드
    def cut_prev(self):
        if self.prev_box == None:
            return

        self.prev_box.next_box = None
        self.prev_box = None

    # 연결리스트 중간에서 노드를 빼오는 메서드
    def take_out(self):
        if self.next_box:
            self.next_box.prev_box = self.prev_box
        if self.prev_box:
            self.prev_box.next_box = self.next_box

        self.next_box = None
        self.prev_box = None


class Belt:
    # 첫 상자와 끝 상자를 가리킬 변수와
    # 상자 ID 검색을 빠르게 하기 위한 딕셔너리 box_dict,
    # 벨트 고장 여부를 저장할 broken을 선언
    def __init__(self):
        self.first_box: Box = None
        self.last_box: Box = None
        self.box_dict: dict = dict()
        self.broken: bool = False

    # 벨트 끝에 상자를 추가하는 메서드
    # 끝 상자와 추가할 상자를 이어주고, 벨트의 끝 상자를 추가한 상자로 바꾼다.
    # 상자가 없을 때 호출 된다면, 첫 상자를 해당 상자로 설정한다.
    def add_box(self, this_box: Box):
        self.box_dict[this_box.box_id] = this_box  # box id : box 데이터

        if not self.first_box:
            self.first_box = this_box

        if self.last_box:
            self.last_box.set_next(this_box)
            this_box.set_prev(self.last_box)

        self.last_box = this_box

    # 벨트 가장 앞 상자를 빼는 메서드
    # 두 번째 상자를 첫 상자로 바꾸고, 앞 상자와의 연결을 끊어준다.
    # 상자가 1개 일 때 호출 된다면 끝 상자도 None으로 바꿔준다.
    def pop_box(self):
        box_to_pop = self.first_box
        self.first_box = box_to_pop.next_box

        if self.first_box:
            self.first_box.cut_prev()
        else:
            self.last_box = None

        del self.box_dict[box_to_pop.box_id]

        return box_to_pop


class Factory:
    # 100 연산이자 생성자. 매개변수로 100을 제외한 모든 숫자를 받는다.
    # N, M을 분리시키고, 한 벨트당 몇 개의 상자가 들어갈지 계산해 counts에 저장
    # M개의 벨트를 만들고, presents에서 counts 만큼의 연속된 정보로 box를 생성해 벨트에 추가
    def __init__(self, args):
        N, M, *presents = args
        counts = N // M
        self.belts = [Belt() for _ in range(M)]

        for idx, belt in enumerate(self.belts):
            for num in range(idx * counts, (idx + 1) * counts):
                belt.add_box(Box(presents[num], presents[num + N]))

    # 200 연산. max_weight을 매개변수로 받고, 기본 반환값은 0
    # 벨트를 모두 돌면서 first_box가 있는 경우, pop_box 메서드로 일단 빼온다.
    # 빼온 상자가 max_weight 이하면 result에 무게를 더하고,
    # 아니라면 add_box 메서드 뒤에 그대로 다시 추가
    def unload(self, max_weight):
        result = 0

        for belt in self.belts:
            if belt.first_box:
                popped_box = belt.pop_box()
                if popped_box.weight <= max_weight:
                    result += popped_box.weight

                else:
                    belt.add_box(popped_box)

        return result

    # 300 연산. 제거할 id를 매개변수로 받고, 기본 반환값은 -1
    # 벨트를 돌면서 딕셔너리에 id가 있는지 확인
    # id를 발견하면 해당 상자가 벨트의 처음, 끝 상자인지 확인해 처리,
    # take_out 메서드로 연결 리스트에서 빼준다.
    # 딕셔너리에서는 id로 제거
    def remove(self, remove_id):
        result = -1

        for belt in self.belts:
            if remove_id in belt.box_dict:
                removed_box: Box = belt.box_dict[remove_id]

                if belt.first_box == removed_box:
                    belt.first_box = removed_box.next_box
                if belt.last_box == removed_box:
                    belt.last_box = removed_box.prev_box

                removed_box.take_out()
                result = removed_box.box_id
                del belt.box_dict[removed_box.box_id]
                break

        return result

    # 400 연산. 찾을 id를 매개변수로 받고, 기본 반환값은 -1
    # 벨트를 돌면서 상자 찾기. 반환 값이 벨트의 아이디(인덱스 + 1) 라서 enumerate 사용
    # 상자를 찾으면, 그 위치가 벨트의 처음이 아닐 경우, 첫 상자와 끝 상자를 이어주고
    # 찾은 상자를 첫 상자로, 그 앞 상자를 끝 상자로 바꿔주고 둘의 연결을 끊으면 된다.
    def find(self, find_id):
        result = -1

        for belt_id, belt in enumerate(self.belts):
            if find_id in belt.box_dict:
                found_box: Box = belt.box_dict[find_id]

                if belt.first_box != found_box:
                    belt.first_box.set_prev(belt.last_box)
                    belt.last_box.set_next(belt.first_box)

                    belt.first_box = found_box
                    belt.last_box = found_box.prev_box

                    found_box.cut_prev()

                result = belt_id + 1
                break

        return result

    # 500 연산. 고장시킬 벨트의 id를 매개변수로 받고, 기본 반환값 -1
    # 만약 이미 고장난 벨트가 아닐 경우, 반환 값을 벨트 id로 바꾸고, 고장 상태를 True
    # 그리고 그 위에 상자가 있을 경우, 고장 벨트 다음 벨트부터 차례로 돌며 정상 벨트 찾고
    # 고장 벨트의 딕셔너리 내용을 정상 벨트 딕셔너리에 추가,
    # 고장 벨트 첫 상자와 정상 벨트 끝 상자를 이어주고,
    # 정상 벨트 끝 상자를 고장 벨트 끝 상자로 바꿔주면 된다.
    # 고장 벨트의 첫 상자와 끝 상자도 잊지 않고 초기화
    def die(self, belt_id):
        result = -1
        belt_id -= 1

        if self.belts[belt_id].broken == False:
            result = belt_id + 1

            broken_belt: Belt = self.belts[belt_id]
            broken_belt.broken = True

            if len(broken_belt.box_dict):
                for idx in range(belt_id, belt_id + len(self.belts)):
                    if self.belts[idx % len(self.belts)].broken == False:  # 정상 벨트 찾기
                        found_belt: Belt = self.belts[idx % len(self.belts)]

                        found_belt.box_dict.update(broken_belt.box_dict)
                        broken_belt.box_dict = {}

                        found_belt.add_box(broken_belt.first_box)
                        found_belt.last_box = broken_belt.last_box
                        broken_belt.first_box = broken_belt.last_box = None
                        break

        return result


if __name__ == "__main__":
    Q = int(input().strip())

    # 첫 줄은 무조건 100 연산이므로, 해당 입력으로 Factory를 생성
    query, *args = map(int, input().split())
    factory = Factory(args)

    # if else 보다 효율적 연산 수행
    queries = {
        200: factory.unload,
        300: factory.remove,
        400: factory.find,
        500: factory.die,
    }

    for _ in range(Q - 1):
        query, arg = map(int, input().split())
        print(queries[query](arg))
