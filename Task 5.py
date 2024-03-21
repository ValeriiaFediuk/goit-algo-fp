import uuid
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1, colors=None):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1, colors=colors)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1, colors=colors)
        if colors is not None:
            colors.append(node.color)
    return graph

def draw_heap(heap_root):
    heap = nx.DiGraph()
    pos = {heap_root.id: (0, 0)}
    colors = []
    heap = add_edges(heap, heap_root, pos, colors=colors)

    # Generate colors from dark to light
    cmap = plt.cm.get_cmap('Blues', len(colors))
    color_mapping = {colors[i]: cmap(i) for i in range(len(colors))}

    for node_id, node_attrs in heap.nodes(data=True):
        node_attrs['color'] = color_mapping[node_attrs['color']]

    labels = {node[0]: node[1]['label'] for node in heap.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(heap, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=list(color_mapping.values()))
    plt.show()

def build_heap(heap_array):
    if not heap_array:
        return None

    def heapify(heap, idx):
        left = 2 * idx + 1
        right = 2 * idx + 2
        largest = idx

        if left < len(heap) and heap[left].val > heap[largest].val:
            largest = left

        if right < len(heap) and heap[right].val > heap[largest].val:
            largest = right

        if largest != idx:
            heap[idx], heap[largest] = heap[largest], heap[idx]
            heapify(heap, largest)

    heap = [Node(val, color=f'#{hex(0x1296F0 + i * 10000)[3:]}') for i, val in enumerate(heap_array)]
    for i in range(len(heap) // 2 - 1, -1, -1):
        heapify(heap, i)

    root = heap[0]
    for i in range(len(heap)):
        left_idx = 2 * i + 1
        right_idx = 2 * i + 2

        if left_idx < len(heap):
            heap[i].left = heap[left_idx]
        if right_idx < len(heap):
            heap[i].right = heap[right_idx]

    return root

heap_array = [1, 2, 3, 4, 5, 6, 7]
heap_tree_root = build_heap(heap_array)
draw_heap(heap_tree_root)
