#ifndef AVLTREE
#define AVLTREE

#include <iostream>
#include <vector>
#include <queue>
using namespace std;

class AVL_tree{
    int key;
    unsigned int height;
    AVL_tree* left;
    AVL_tree* right;
public:
    AVL_tree(int k);

    AVL_tree(AVL_tree* p);

//Поиск элемента.
    AVL_tree* find (int k);

//Размеры дерева.
    unsigned int get_height();

protected:
    void fix_height();

public:
    int balance_factor();

//Балансировка.
protected:
    AVL_tree* turn_right();
    AVL_tree* turn_left();
public:
    AVL_tree* balance();

//Вставка элемента.
    AVL_tree* insert_key(int k);

//Печать дерева. Дерево как бы лежит на боку (растет слева направо).
    void print_tree(int level);

//Обходы деревьев.
//Прямой.
    vector<int> PreOrder(vector<int> path);

//Обратный.
    vector<int> PostOrder(vector<int> path);

//Симметричный
    vector<int> InOrder(vector<int> path);

//В ширину.
    vector<int> LevelOrder();

//Объединение деревьев.
    AVL_tree* union_tree(AVL_tree A);

//Удаление элемента.
protected:
    AVL_tree* del_minus1234();

    int find_max();

    vector<int> subtree_max();
public:
    AVL_tree* delete_key(int k);
};

#endif // AVLTREE

