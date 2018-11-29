package com.example.lab.metamaths;

import android.util.Log;

import com.google.firebase.firestore.EventListener;
import com.google.firebase.firestore.FirebaseFirestore;
import com.google.firebase.firestore.FirebaseFirestoreException;
import com.google.firebase.firestore.QueryDocumentSnapshot;
import com.google.firebase.firestore.QuerySnapshot;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.Random;

import javax.annotation.Nullable;

import de.blox.graphview.Graph;
import de.blox.graphview.GraphAdapter;
import de.blox.graphview.Node;
import de.blox.graphview.energy.FruchtermanReingoldAlgorithm;

public class ShowGraph extends GraphActivity {

    private static final String TAG = "ShowGraph";

    private FirebaseFirestore db;

    public static Map<String, Node> map = new HashMap<>();
    public static Map<String, Model> map1 = new HashMap<>();

    @Override
    public Graph createGraph(ArrayList<String> nodes_values, ArrayList<Model> nodes_data) {

        final Graph graph = new Graph();


        for (int i = 0; i < nodes_values.size(); i++) {
            final Node temp = new Node(nodes_values.get(i));
            map.put(nodes_values.get(i), temp);
            map1.put(nodes_values.get(i), nodes_data.get(i));


            final ArrayList<String> temp_in_edges = nodes_data.get(i).getIn_edges();
            final ArrayList<String> temp_out_edges = nodes_data.get(i).getOut_edges();



            final ArrayList<String> concat_list = new ArrayList<>();
            if (temp_in_edges!=null) {
                if (temp_in_edges.size()>0) {
                    //concat_list.addAll(temp_in_edges);
                    for (int j = 0; j < temp_in_edges.size(); j++) {
                        concat_list.add(temp_in_edges.get(j));
                    }
                }
            }
            if (temp_out_edges!=null)  {
                if (temp_out_edges.size()>0) {
                    for (int j = 0; j < temp_out_edges.size(); j++) {
                        concat_list.add(temp_out_edges.get(j));
                    }
                }
            }


            for (int j = 0; j < concat_list.size(); j++) {

                final Node temp1;

                if (map.containsKey(concat_list.get(j))) {
                    temp1 = map.get(concat_list.get(j));
                    graph.addEdge(temp, temp1);
                } else {
                    temp1 = new Node(concat_list.get(j));
                    map.put(concat_list.get(j), temp1);
                    map1.put(nodes_values.get(i), nodes_data.get(i));
                }
                graph.addEdge(temp, temp1);
                Log.i(TAG, temp + "createGraph: " + new Node(concat_list.get(j)));
            }
        }

        /*for (int i = 1; i< nodes_values.size(); i++) {
            final Node temp = new Node(nodes_values.get(i));
            final ArrayList<String> temp_in_edges = nodes_data.get(i).getIn_edges();
            final ArrayList<String> temp_out_edges = nodes_data.get(i).getOut_edges();
            final ArrayList<String> concat_list = new ArrayList<>();
            concat_list.addAll(temp_in_edges);
            concat_list.addAll(temp_out_edges);

            for (int j = 0; j < concat_list.size(); j++) {
                graph.addEdge(temp, new Node(concat_list.get(j)));
                //graph.addEdge(new Node(getNodeText()), new Node(getNodeText()));
                Log.i(TAG, temp + "createGraph: " + new Node(concat_list.get(j)));
            }

            Log.i(TAG, "createGraph: \n\n\nn\n\n");

        }*/


        return graph;
    }

    @Override
    public void setAlgorithm(GraphAdapter adapter) {
        adapter.setAlgorithm(new FruchtermanReingoldAlgorithm(1000));
    }
}
