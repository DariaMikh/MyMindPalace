#include "avl-tree.h"

int main(void)
{
    AVL_tree A(7);
    AVL_tree* Tree=&A;

    Tree=Tree->insert_key(1);
    Tree=Tree->insert_key(2);
    Tree=Tree->insert_key(3);
    Tree=Tree->insert_key(4);
    Tree=Tree->insert_key(5);
    Tree=Tree->insert_key(8);
    Tree=Tree->insert_key(9);
    Tree=Tree->insert_key(10);

    cout<<"Tree:\n";
    Tree->print_tree(0);
    cout<<endl;

    vector<int> path;
    path=Tree->InOrder(path);
    cout<<"Tree.InOrder:\t ";
    for (vector<int>::iterator i=path.begin(); i!=path.end(); i++){
        cout<<*i<<" ";
    }
    cout<<endl;

    path.clear();
    path=Tree->PostOrder(path);
    cout<<"Tree.PostOrder:\t ";
    for (vector<int>::iterator i=path.begin(); i!=path.end(); i++){
        cout<<*i<<" ";
    }
    cout<<endl;

    path.clear();
    path=Tree->PreOrder(path);
    cout<<"Tree.PreOrder:\t ";
    for (vector<int>::iterator i=path.begin(); i!=path.end(); i++){
        cout<<*i<<" ";
    }
    cout<<endl;

    path.clear();
    path=Tree->LevelOrder();
    cout<<"Tree.LevelOrder: ";
    for (vector<int>::iterator i=path.begin(); i!=path.end(); i++){
        cout<<*i<<" ";
    }
    cout<<endl;

    AVL_tree B(55);
    B.insert_key(50);
    B.insert_key(60);
    B.insert_key(45);
    cout<<"\nB: \n";
    B.print_tree(0);
    cout<<endl<<endl;

    cout<<"Union Tree and B:\n";
    AVL_tree* union_tree=Tree->union_tree(B);
    union_tree->print_tree(0);
    cout<<endl<<endl;

    int bfactor=B.balance_factor();
    int height=union_tree->get_height();
    cout<<"Balance factor of B= "<<bfactor;
    cout<<"\nHeight of union_tree= "<<height;

    cout<<"\n\nFind 50 in union_tree:\n";
    AVL_tree* find=union_tree->find(50);
    find->print_tree(0);

    cout<<endl<<"Tree:\n";
    Tree->print_tree(0);

    cout<<"After delete 4\n";
    Tree=Tree->delete_key(4);
    Tree->print_tree(0);
    cout<<"After delete 2\n";
    Tree=Tree->delete_key(2);
    Tree->print_tree(0);
    cout<<"After delete 1\n";
    Tree=Tree->delete_key(1);
    Tree->print_tree(0);
    cout<<"After delete 8\n";
    Tree=Tree->delete_key(8);
    Tree->print_tree(0);

    system("pause");
    return 0;
}

