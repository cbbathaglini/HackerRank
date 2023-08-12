import java.io.*;
import java.util.*;

class Tree {
    private List<TreeLeaf> leafs;
    private List<TreeNode> node;
}

class TreeLeaf {
    private Integer numero;
    private Integer peso;
    private Boolean visited = false;
    private Integer color;
    private TreeNode nodePai;

    public TreeLeaf(Integer numero, Integer peso, Integer color) {
        this.numero = numero;
        this.peso = peso;
        this.visited = false;
        this.color = color;
    }

    public Integer getNumero() {
        return this.numero;
    }

    public Integer getPeso() {
        return this.peso;
    }

    public Boolean getVisited() {
        return this.visited;
    }
}

class Arestas{
    private Integer noA;
    private Integer noB;
    
    public Arestas
}

class TreeNode {

}

interface TreeInterface {
    Integer getResult();

    void visitNode(TreeNode node);

    void visitLeaf(TreeLeaf leaf);
}

class SumInLeavesVisitor implements TreeInterface {
    private Tree tree;

    public SumInLeavesVisitor(Tree tree) {
        this.tree = tree;
    }

    // somar apenas as folhas
    @Override
    public Integer getResult() {
        return 0;
    }

    @Override
    public void visitNode(TreeNode node) {

    }

    @Override
    public void visitLeaf(TreeLeaf leaf) {

    }

}

class ProductRedNodesVisitor {

}

class FancyVisitor {

}

public class Solution {

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        //1) ler o numero de nos = n
        Integer n = s.nextInt();
        System.out.println("n: "+ n);
        
        s.nextLine();
        
        //2) valores dos nos (array)
        String valores_nos = s.nextLine();
        System.out.println("valores_nos: "+ valores_nos);
        
        //3) cores dos nos (array) 
        //   -> 0 red 
        //   -> 1 green
        String cores_nos = s.nextLine();
        System.out.println("cores_nos: "+ cores_nos);
        
        
        //4) proximas n-1 linhas arestas entre os nos
        List<Integer,Integer> arestas = new ArrayList<>()
        String[] arestas_str = new String[n-1];
        int contador = 0;
        while(s.hasNext()){
            arestas_str[contador] = s.nextLine();
            System.out.println("n: "+arestas_str[contador]);
            contador++;
        }
        
        
        //carregando os nos
        
        
        Tree tree = new Tree();
        TreeInterface sumInLeavesVisitor = new SumInLeavesVisitor(tree);
        System.out.println(sumInLeavesVisitor.getResult());
       
    }
}