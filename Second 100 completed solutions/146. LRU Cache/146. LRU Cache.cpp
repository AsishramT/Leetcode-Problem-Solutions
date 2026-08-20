class Node {
public:
    int key;
    int val;
    Node* next;
    Node* prev;

    Node(int key=0, int val=0){
        this->key=key;
        this->val=val;
        this->next=nullptr;
        this->prev=nullptr;
    }

};

class LRUCache {
public:
    int cap;
    unordered_map<int, Node*> cache;
    Node* left;
    Node* right;

    LRUCache(int capacity) {
        cap = capacity;
        cache={};

        left = new Node();
        right = new Node();

        left->next=right;
        right->prev=left;

    }
    
    int get(int key) {
        //if not found
        if (cache.find(key) == cache.end()) {
            return -1;
        }

        Node* node = cache[key];

        remove(node);
        insert(node);

        return node->val;
    }
    
    void put(int key, int value) {
        if(cache.find(key) != cache.end()){
            remove(cache[key]);
            cache.erase(key);
        }
        
        Node* node= new Node(key,value);
        cache[key]=node;
        insert(node);

        if (cap < cache.size()){
            Node* LRU = left->next;
            remove(LRU);
            cache.erase(LRU->key);
        }
        
    }

    void insert(Node* node){
        Node* prev = right->prev;

        prev->next=node;
        node->prev=prev;

        node->next=right;
        right->prev=node;
    }

    void remove(Node* node){
        Node* prev = node->prev;
        Node* next = node->next;

        prev->next = next;
        next->prev = prev;
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */