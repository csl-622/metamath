package com.example.lab.metamaths;

import android.content.Context;
import android.content.Intent;
import android.support.annotation.NonNull;
import android.support.v7.widget.RecyclerView;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;

import java.util.List;

public class ChaptersAdapter extends RecyclerView.Adapter<ChaptersAdapter.VHChapters> {

    private List<Chapter> chapters;
    private Context context;

    public ChaptersAdapter(List<Chapter> chapters, Context context) {
        this.chapters = chapters;
        this.context = context;
    }

    @NonNull
    @Override
    public VHChapters onCreateViewHolder(@NonNull ViewGroup parent, int i) {
        View itemView = LayoutInflater.from(parent.getContext())
                .inflate(R.layout.chapter_list_item, parent, false);

        return new VHChapters(itemView);
    }

    @Override
    public void onBindViewHolder(@NonNull final VHChapters vhChapters, final int i) {
        vhChapters.setBookNumber(chapters.get(i).getChapterName());
        vhChapters.setOpenGraph(chapters.get(i).getGraph());

        vhChapters.itemView.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                Intent intent = new Intent(new Intent(context, PdfActivity.class));
                switch (i) {
                    case 0:
                        intent.putExtra("start", 4);
                        intent.putExtra("end", 47);
                        break;
                    case 1:
                        intent.putExtra("start", 48);
                        intent.putExtra("end", 67);
                        break;
                    case 2:
                        intent.putExtra("start", 68);
                        intent.putExtra("end", 107);
                        break;
                    case 3:
                        intent.putExtra("start", 108);
                        intent.putExtra("end", 127);
                        break;
                    case 4:
                        intent.putExtra("start", 128);
                        intent.putExtra("end", 153);
                        break;
                    case 5:
                        intent.putExtra("start", 154);
                        intent.putExtra("end", 191);
                        break;
                    case 6:
                        intent.putExtra("start", 192);
                        intent.putExtra("end", 225);
                        break;
                    case 7:
                        intent.putExtra("start", 226);
                        intent.putExtra("end", 251);
                        break;
                    case 8:
                        intent.putExtra("start", 252);
                        intent.putExtra("end", 279);
                        break;
                    case 9:
                        intent.putExtra("start", 280);
                        intent.putExtra("end", 421);
                        break;

                    case 10:
                        intent.putExtra("start", 422);
                        intent.putExtra("end", 469);
                        break;
                    case 11:
                        intent.putExtra("start", 470);
                        intent.putExtra("end", 503);
                        break;
                    case 12:
                        intent.putExtra("start", 504);
                        intent.putExtra("end", 537);
                        break;
                    default:
                        intent.putExtra("start", 1);
                        intent.putExtra("end", 545);
                        break;

                }
                vhChapters.itemView.getContext().startActivity(intent);
            }
        });

        vhChapters.openGraph.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(context, ShowGraph.class);
                intent.putExtra("book_number", chapters.get(i).getChapterName());
                vhChapters.openGraph.getContext().startActivity(intent);
            }
        });
    }

    @Override
    public int getItemCount() {
        return chapters.size();
    }

    public class VHChapters extends RecyclerView.ViewHolder {

        private TextView bookNumber;
        private ImageView  openGraph;

        public VHChapters(@NonNull View itemView) {
            super(itemView);

            bookNumber = itemView.findViewById(R.id.book_number);
            openGraph = itemView.findViewById(R.id.open_graph);
        }

        public void setBookNumber(String bookNumber_s) {
            bookNumber.setText(bookNumber_s);
        }

        public void setOpenGraph(int image) {
            openGraph.setImageResource(image);
        }
    }
}
