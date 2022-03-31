#include<iostream>
// Index is a data structure able to provide all this features:
// - Adding new data, Searching data, Removing data

/**
 * Successor of a Node:
 * - The next value of the key of the node
 * 
 * - if the node is a leaf: we need to find the maximum (right parent)
 * - I go up until i move to the right, this is the successor.
 */
class BinarySearchTree {
    struct Node {
        int key;
        Node* left;
        Node* right;
    };

    private:
        Node* root;

        Node* insert(int k, Node* node) {
            if (node == NULL) {
                node = new Node;
                node -> key = k;
                node -> left = NULL;
                node -> right = NULL;
            } else if (k < node -> key) {
                node -> left = insert(k, node -> left);
            } else if (k > node -> key) {
                node -> right = insert(k, node -> right);
            }
            return node;
        }

        void inOrder(Node* node) {
            if (node != NULL) {
                inOrder(node -> left);
                std::cout << node -> key;
                inOrder(node -> right);
            }
        }

    public:

        BinarySearchTree() {
            root = NULL;
        }

        Node* insert(int k) {
            return insert(k, root);
        }

        void inOrder() {
            inOrder(root);
        }

};

// Binary Search Tree
int main () {
    BinarySearchTree bst;
    bst.insert(10);
    bst.insert(20);

    bst.inOrder();
    return 0;
}