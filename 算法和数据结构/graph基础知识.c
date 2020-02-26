//  无向图表示法:
// G(v1, {E1}) v1={A,B,C,D} E1={(a,b),(B,C),(D,A),(A,C)}
//  有向图表示法:
// G(v2, {E2}) v1={A,B,C,D} E1={<a,b>,<B,C>,<D,A>,<A,C>}

// 无向图：边数之和等于各个顶点度数之和的一半
// 有向图：边数之和等于各个顶点度数之和

// 连通图: 图中任意两顶点都是连同的（及有路径相通）
// 强连通图：vi->vj,vj->vi都有路径（有向图）
// 极大连通子图：连通子图含有极大顶点数

/* 存储结构:{
1,邻接矩阵
2，邻接表
3, 边集数组
}
*/
/* 深度优先:{
    DFS
    类似于树的先序遍历。添加个标记visited[i].
}
*/
/* 广度优先:{
    BFS
    类似于树的层序遍历
}
*/
/*
最小生成树
求连通图的最小生成树:
普利姆算法：
克卢卡尔算法：
基本思想：（1）构造一个只含n个顶点，边集为空的子图。
若将图中各个顶点看成一棵树的根节点，则它是一个含有n棵树的森林。
（2）从网的边集 E 中选取一条权值最小的边，若该条边的两个顶点分属不同的树，
则将其加入子图。也就是说，将这两个顶点分别所在的两棵树合成一棵树；
反之，若该条边的两个顶点已落在同一棵树上，则不可取，
而应该取下一条权值最小的边再试之
（3）依次类推，直至森林中只有一棵树，也即子图中含有 n-1条边为止。

大白话： （1）将图中的所有边都去掉。
        （2）将边按权值从小到大的顺序添加到图中，保证添加的过程中不会形成环
        （3）重复上一步直到连接所有顶点，此时就生成了最小生成树。这是一种贪心策略。
*/

/*
最短路径
地杰斯特拉算法

*/

/*
拓扑排序
in-data-firstdge
*/
// 邻接矩阵

typedef char VertexType;
typedef int EdgeType;
#define MAXVEX 100
#define INFINITY 65535

typedef struct{
//    顶点表
    VertexType vexs[MAXVEX];
//    边表
    EdgeType arc[MAXVEX][MAXVEX];
    int numVertexes, numEdges;
}MGraph;

// 无向图生成
void BreateMGraph(MGraph *G){
    int i, j, k, w;
    printf("顶点数，边数\n");
    scanf("%d, %d", &G->numVertexes, &G->numEdges);
    for(i = 0; i < G->numVertexes; i++){
        scanf(&G->vexs[i]);
    }
    for(i = 0; i < G->numVertexes; i++){
        for(j = 0; j < G->numVertexes; j++){
            G->arc[i][j] = INFINITY;
        }
    }
    for(k = 0; k < G->numEdges; k++){
        printf("输入边的坐标和权值");
        scanf("%d, %d, %d", &i, &j, &w);
        G->arc[i][j] = w;
        G->arg[j][i] = G->arc[i][j];
    }
}

// 邻接表
typedef char VertexType;
typedef int EdgeType;

typedef struct EdgeNode{
    int adjvex;
    EdgeType weight;
    struct EdgeNode *next;
}EdgeNode;

typedef struct VertextNode{
    VertexType data;
    EdgeNode *firstedge;
}VertextNode, AdjList[MAXVEX];

typedef struct{
    AdjList adjList;
    int numVertexes, numEdges;
}GraphAdjList;

void createALGraph(GraphAdjList *G){
    int i, j, k;
    EdgeNode *e;
    printf("输入定点数，边数");
    scanf("%d, %d", &G->numVertexes, &G->numEdges);
    for(i = 0; i < G->numVertexes; i++){
        scanf(&G->adjList[i].data);
        G->adjList[i].firstedge = NULL;
    }
    for(k = 0; k < G->numEdges; k++){
        printf("\n");
        scanf("%d, %d", &i, &j);
        e = (EdgeNode *)malloc(sizeof(EdgeNode));
        e->adjvex = j;
        e->next = G->adjvex[i].firstedge;
        G->adjList[i].firstedge = e;
    }
}

// 深度优先遍历（DFS）之矩阵

typedef int Boolean;
Boolean visited[MAX];

void DFS(MGraph G, int i){
    int j;
    visited[i] = TRUE;
    printf("%c", G.vexs[i]);
    for(j = 0; j < G.numVertexes; j++){
        if(G[i][j] == 1 && !visited[j]){
            DFS（G, j);
        }
    }
}

// 深度优先遍历（DFS）之邻接表
void DFS2(GraphAdjList GL, int i){
    EdgeNode *p;
    visited[i] = TRUE;
    printf("%c", GL->adjList[i].data);
    p = GL->adjList[i].firstedge;
    while(p){
        if(!visited[p->adjvex]){
            DFS2(GL, p->adjvex);
        }
        p = p->next;
    }
}

void DFSTraverse(GraphAdjList GL){
    int i;
    for(i = 0; i < GL->numVertexes; i++){
        visited[i] = FALSE;
    }
    for(i = 0; i < GL->numVertexes; i++){
        if(!visited[i]){
            DFS2(GL, i);
        }
    }
}

// 广度优先之邻接矩阵
void BFSTraverse(MGraph G){
    int i, j;
    Queue Q;
    for(i = 0; i < G.numVertexes; i++){
        visited[i] = FALSE;
    }
    InitQueue(&Q);
    for(i = 0; i < G.numVertexes; i++){
        if(!visited[i]){
            visited[i] = TRUE;
            printf("%c", G.vexs[i]);
            EnQueue(&Q, i);
            while(!QueueEmpty(Q)){
                DeQueue(&Q, &i);
                for(j = 0; j < G.numVertexes; j++){
                    if(G.arc[i][j] == 1 && !visited[j]){
                        visited[j] = TRUE;
                        printf("%c", G.vexs[j]);
                        EnQueue(&Q, j);
                    }
                }
            }
        }
    }
}

// 广度优先之邻接表
void BTSTraverse2(GraphAdjList GL){
    int i;
    EdgeNode *p;
    Queue Q;
    for(i=0; i<GL->numVertexes; i++){
        visited[i] = FALSE;
    }
    InitQueue(&Q);
    for(i = 0; i < GL->numVertexes; i++){
        if(!visited[i]){
            visited[i] = TRUE;
            printf("%c", GL->adjList[i].data);
            EnQueue(&Q, i);
            while(!QueueEmpty(Q)){
                DeQueue(&Q, &i);
                p = GL->adjList[i].firstedge;
                while(p){
                    if(!visited[p->adjvex]){
                        visited[p->adjvex] = TRUE;
                        printf("%c", GL->adjList[p->adjvex].data);
                        EnQueue(&Q, p->adjvex);
                    }
                    p = p->next;
                }
            }
        }
    }
}

// Prim算法
// 设置v0为初始顶点，定义一个访问集合每次添加....
void MiniSpanTree_Prim(MGraph G){
    int min, i, j, k;
    int ajvex[MAXVEX];
    int lowcost[MAXVEX];
    lowcost[0] = 0;
    adjvex[0] = 0;
    for(i = 1; i < G.numVertexes; i++){
        lowcost[i] = G.arc[0][i];
        adjvex[i] = 0;
    }
    for(i = 1; i < G.numVertexes; i++){
        min = INFINITY;
        j = 1; k = 0;
        while(j < G.numVertexes){
            if(lowcost[j] != 0 && lowcost[j] < min){
                min = lowcost[j];
                k = j;
            }
            j++;
        }
        printf("(%d,%d)", adjvex[k], k);
        lowcost[k] = 0;
        for(j = 1; j < G.numVertexes; j++){
            if(lowcost[j] != 0 && G.arc[k][j] < lowcost[j]){
                lowcost[j] = G.arc[k][j];
                adjvex[j] = k;
            }
        }
    }

}

// 克鲁斯卡尔算法
typedef struct{
    int begin;
    int end;
    int weight;
}Edge;

void MiniSpanTree_Kruskal(MGraph G){
    int i, n, m;
    Edge edges[MAXEDGE];
    int parent[MAXVEX];

    for(i = 0; i < G.numVertexes; i++){
        parent[i] = 0;
    }
    for(i = 0; i < G.numEdges; i++){
        n = Find(parent, edges[i].begin);
        m = Find(parent, edges[i].end);
        if(n != m){
            parent[n] = m;
            printf("(%d,%d)%d",edges[i].begin,
                edges[i].end, edges[i].weight)
        }
    }
}

int Find(int *parent, int f){
    while(parent[f] > 0){
        f = parent[f];
        return f;
    }
}

// 地杰斯特拉算法
# define MAXVEX 9
# define INFINITY 65535
// 存储最短路径下标的数组
typedef int Pathmatirx[MAXVEX];
// 存储各点最短路径的权值和
typedef int ShortPathTable[MAXVEX];

void ShortestPath_Dijkstra(MGraph G, int v0, Pathmatirx *P,
    ShortPathTable *D){
    int v, w, k, min;
    int final[MAXVEX];
    for(v = 0; v < G.numVertexes; v++){
        final[v] = 0;
        (*D)[v] = G.matirx[v0][v];
        (*p)[v] = 0;
    }
    (*D)[v0] = 0;
    final[v0] = 1;
    for(v=1; v<G.numVertexes; v++){
        min=INFINITY;
        for(w=0; w<G.numVertexes; w++){
            if(!final[w] && (*D)[w] < min){
                k = w;
                min = (*D)[w];
            }
        }
        final[k] = 1;
        for(w=0; w<G.numVertexes; w++){
            if(!final[w] && (min+G.matirx[k][w] < (*D)[w])){
                (*D)[w] = min + G.matirx[k][w];
                (*P)[w] = k;
            }
        }
    }
}

// 拓扑排序
typedef struct EdgeNode{
    int adjvex;
    int weight;
    struct EdgeNode *next;
}EdgeNode;

typedef struct VertextNode{
    int in;
    int data;
    EdgeNode *firstedge;
}VertextNode, AdjList[MAXVEX];

typedef struct{
    AdjList adjList;
    int numVertexes, numEdges;
}graphAdjList, *GraphAdjList;

Status TopologicalSort(GraphAdjList GL){
    EdgeNode *e;
    int i, k, gettop;
    int top = 0;
    int count = 0;
    int *stack;
    stack = (int *)malloc(GL->numVertexes * sizeof(int))
    // 入度为0的顶点入栈
    for(i = 0; i < GL->numVertexes; i++){
        if(GL->adjList[i].in == 0){
            stack[++top] = i;
        }
    }
    while(top != 0){
        gettop = stack[top--]
        printf('%d->', GL->adjList[gettop].data)
        count++
        for(e=GL->adjList[gettop].firstedge; e; e=e->next){
            k = e->adjvex;
            if(!(--GL->adjList[k].in)){
                stack[++top] = k;
            }
        }
        if(count < GL->numVertexes)
            return ERROR;
        else:
            return OK;
    }
}

