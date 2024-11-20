class Node:
    """Clase para un nodo del Árbol de Búsqueda Binaria (ABB)."""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    """Clase para manejar un Árbol de Búsqueda Binaria."""
    def __init__(self):
        self.root = None

    def insert(self, value):
        """Inserta un valor en el ABB."""
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current, value):
        """Inserta un valor recursivamente."""
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
            else:
                self._insert_recursive(current.left, value)
        elif value > current.value:
            if current.right is None:
                current.right = Node(value)
            else:
                self._insert_recursive(current.right, value)

    def inorder_traversal(self):
        """Realiza un recorrido en orden del ABB."""
        result = []
        self._inorder_traversal_recursive(self.root, result)
        return result

    def _inorder_traversal_recursive(self, current, result):
        if current:
            self._inorder_traversal_recursive(current.left, result)
            result.append(current.value)
            self._inorder_traversal_recursive(current.right, result)


class BTreeNode:
    """Clase para un nodo del Árbol B."""
    def __init__(self, t):
        self.t = t  # Grado mínimo
        self.keys = []  # Claves en el nodo
        self.children = []  # Hijos del nodo
        self.leaf = True  # Indica si el nodo es hoja

    def split_child(self, i, y):
        """Divide un hijo lleno."""
        t = self.t
        z = BTreeNode(t)
        z.leaf = y.leaf
        z.keys = y.keys[t:]  # Copia la mitad derecha de las claves
        if not y.leaf:
            z.children = y.children[t:]  # Copia los hijos correspondientes
        y.keys = y.keys[:t - 1]  # Mantiene la mitad izquierda en y
        y.children = y.children[:t]  # Ajusta los hijos de y
        self.children.insert(i + 1, z)
        self.keys.insert(i, y.keys.pop(-1))

    def insert_non_full(self, key):
        """Inserta una clave en un nodo no lleno."""
        i = len(self.keys) - 1
        if self.leaf:
            # Insertar en un nodo hoja
            self.keys.append(None)
            while i >= 0 and key < self.keys[i]:
                self.keys[i + 1] = self.keys[i]
                i -= 1
            self.keys[i + 1] = key
        else:
            # Encontrar el hijo donde insertar
            while i >= 0 and key < self.keys[i]:
                i -= 1
            i += 1
            if len(self.children[i].keys) == 2 * self.t - 1:
                # Si el hijo está lleno, dividirlo
                self.split_child(i, self.children[i])
                if key > self.keys[i]:
                    i += 1
            self.children[i].insert_non_full(key)


class BTree:
    """Clase para un Árbol B."""
    def __init__(self, t):
        self.root = BTreeNode(t)
        self.t = t

    def insert(self, key):
        """Inserta una clave en el Árbol B."""
        r = self.root
        if len(r.keys) == 2 * self.t - 1:
            # Si la raíz está llena, dividirla
            s = BTreeNode(self.t)
            self.root = s
            s.children.append(r)
            s.leaf = False
            s.split_child(0, r)
            s.insert_non_full(key)
        else:
            r.insert_non_full(key)


# Conjunto A
A = [3, 15, 11, 7, 28, 29, 5, 10, 14, 13, 2, 20, 1, 22, 12, 4, 30, 18, 21, 6, 19, 27]

# 1. Construcción del ABB
bst = BinarySearchTree()
for value in A:
    bst.insert(value)

# Recorrido en orden del ABB
print("ABB (Recorrido en orden):", bst.inorder_traversal())

# 2. Construcción del Árbol B con m = 5
btree = BTree(3)  # m = 5 implica t = 3 (mínimo grado)
for value in A:
    btree.insert(value)

# Visualización simple del Árbol B (Claves en la raíz)
print("Árbol B (Claves en la raíz):", btree.root.keys)
