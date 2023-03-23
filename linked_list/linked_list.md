# Linked List

## 개념 정리

- 노드(`Node`)라는 구조체가 연결되는 형식으로 데이터를 저장하는 자료구조
- 노드는 데이터 값과 다음 노드의 주소값을 저장
- 메모리에는 비연속적으로 저장되지만 각각의 노드가 다음 노드의 메모리 주소값을 가리킴으로써 논리적인 연속성을 가짐

## 조회

### __get_node(index)

- 시간복잡도: O(N)

```python
node = self.head
for _ in range(index):
    node = node.next_
return node
```

- index에 해당하는 노드를 리턴

## 추가

### append(value)

- 시간복잡도: O(1)

```python
if not self.head:
    self.head = new_node
    self.tail = new_node
    return
```

- head가 `None`인지 체크하여 첫 인서트인지 확인
- head와 tail에 new_node를 할당하고 리턴

```python
self.tail.next_ = new_node
self.tail = new_node
```

- tail의 next로 new_node를 할당
- tail이 마지막 노트를 가리키도록 tail에 new_node를 할당

### insert(index, value)

- 시간복잡도: O(N)

```python
prev_node = self.get_node(index - 1)
new_node.next_ = prev_node.next_
prev_node.next_ = new_node
```

- new_node의 next에는 (index-1) 위치에 존재하는 노드의 next를 할당해야하므로 추가할 (index-1) 위치에 존재하는 노드를 찾아옴(prev_node)
- prev_node 노드의 next를 new_node의 next에 할당
- prev_node 노드의 next에 new_node를 할당하여 리스트를 이어줌

## 삭제

### remove(index)

- 시간복잡도: O(N)

```python
prev_node = self.__get_node(index - 1)
next_node = prev_node.next_.next_
prev_node.next_ = next_node
```

- prev_node: 삭제할 위치 바로 이전(index-1)에 존재하는 노드
- next_node: 삭제할 위치 바로 다음(index+1)에 존재하는 노드
- prev_node의 next에 next_node를 할당해서 이어주면 index 노드의 참조가 끊어짐