import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext, ttk
import subprocess
import sys


class SyntheMolGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("SyntheMol Generator GUI")
        self.root.geometry("1000x800")

        self.entries = {}

        self.build_form()
        self.build_run_button()
        self.build_output_console()

    def add_field(self, label, key, row, col, default="", required=False):
        frame = tk.Frame(self.form_frame)
        frame.grid(row=row, column=col, sticky="ew", padx=10, pady=5)

        display_label = label + " (*)" if required else label
        label_widget = tk.Label(frame, text=display_label, width=30, anchor="w")
        if required:
            label_widget.config(font=("TkDefaultFont", 9, "bold"))
        label_widget.pack(side="left")

        entry = tk.Entry(frame)
        entry.insert(0, str(default) if default is not None else "")
        entry.pack(side="left", fill="x", expand=True)

        self.entries[key] = {"widget": entry, "required": required, "label": label}

    def add_file_field(self, label, key, row, col, default="", required=False):
        frame = tk.Frame(self.form_frame)
        frame.grid(row=row, column=col, sticky="ew", padx=10, pady=5)

        display_label = label + " (*)" if required else label
        label_widget = tk.Label(frame, text=display_label, width=30, anchor="w")
        if required:
            label_widget.config(font=("TkDefaultFont", 9, "bold"))
        label_widget.pack(side="left")

        entry = tk.Entry(frame)
        entry.insert(0, str(default) if default is not None else "")
        entry.pack(side="left", fill="x", expand=True)

        def browse():
            file_path = filedialog.askopenfilename()
            if file_path:
                entry.delete(0, tk.END)
                entry.insert(0, file_path)

        tk.Button(frame, text="Browse", command=browse).pack(side="left")

        self.entries[key] = {"widget": entry, "required": required, "label": label}

    def add_dir_field(self, label, key, row, col, default="", required=False):
        frame = tk.Frame(self.form_frame)
        frame.grid(row=row, column=col, sticky="ew", padx=10, pady=5)

        display_label = label + " (*)" if required else label
        label_widget = tk.Label(frame, text=display_label, width=30, anchor="w")
        if required:
            label_widget.config(font=("TkDefaultFont", 9, "bold"))
        label_widget.pack(side="left")

        entry = tk.Entry(frame)
        entry.insert(0, str(default) if default is not None else "")
        entry.pack(side="left", fill="x", expand=True)

        def browse():
            dir_path = filedialog.askdirectory()
            if dir_path:
                entry.delete(0, tk.END)
                entry.insert(0, dir_path)

        tk.Button(frame, text="Browse", command=browse).pack(side="left")

        self.entries[key] = {"widget": entry, "required": required, "label": label}

    def add_checkbox(self, label, key, row, col, default=False):
        var = tk.BooleanVar(value=default)
        chk = tk.Checkbutton(self.form_frame, text=label, variable=var)
        chk.grid(row=row, column=col, sticky="w", padx=10, pady=5)
        self.entries[key] = {"widget": var, "required": False, "label": label}

    def add_dropdown(self, label, key, row, col, options, default=None, required=False):
        frame = tk.Frame(self.form_frame)
        frame.grid(row=row, column=col, sticky="ew", padx=10, pady=5)

        display_label = label + " (*)" if required else label
        label_widget = tk.Label(frame, text=display_label, width=30, anchor="w")
        if required:
            label_widget.config(font=("TkDefaultFont", 9, "bold"))
        label_widget.pack(side="left")

        combo = ttk.Combobox(frame, values=options, state="readonly")
        if default:
            combo.set(default)
        elif options:
            combo.set(options[0])
        combo.pack(side="left", fill="x", expand=True)

        self.entries[key] = {"widget": combo, "required": required, "label": label}

    def build_form(self):
        container = tk.Frame(self.root)
        container.pack(fill="both", expand=True, padx=5, pady=5)

        canvas = tk.Canvas(container)
        scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
        
        self.form_frame = tk.Frame(canvas)
        
        self.form_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=self.form_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        self.form_frame.grid_columnconfigure(0, weight=1)
        self.form_frame.grid_columnconfigure(1, weight=1)
        
        # --- Column 0 (General & Paths, BB Settings) ---
        row_left = 0
        self.add_dropdown("Search Type", "--search_type", row_left, 0, ["mcts", "rl"], default="mcts", required=True); row_left += 1
        self.add_dir_field("Save Directory", "--save_dir", row_left, 0, required=True); row_left += 1
        self.add_dropdown("Chemical Spaces", "--chemical_spaces", row_left, 0, ["real", "wuxi", "custom"], default="real"); row_left += 1
        self.add_file_field("Building Blocks Paths", "--building_blocks_paths", row_left, 0, ""); row_left += 1
        self.add_file_field("Reaction to BB Paths", "--reaction_to_building_blocks_paths", row_left, 0, ""); row_left += 1
        self.add_field("Building Blocks ID Column", "--building_blocks_id_column", row_left, 0, ""); row_left += 1
        self.add_field("Building Blocks Score Columns", "--building_blocks_score_columns", row_left, 0, ""); row_left += 1
        self.add_field("Building Blocks SMILES Column", "--building_blocks_smiles_column", row_left, 0, ""); row_left += 1
        self.add_field("Max Reactions", "--max_reactions", row_left, 0, "1"); row_left += 1
        self.add_field("N Rollout", "--n_rollout", row_left, 0, "10"); row_left += 1
        self.add_field("Explore Weight", "--explore_weight", row_left, 0, "10.0"); row_left += 1
        self.add_field("Num Expand Nodes", "--num_expand_nodes", row_left, 0); row_left += 1
        self.add_field("Save Frequency", "--save_frequency", row_left, 0, "1000"); row_left += 1
        self.add_field("RNG Seed", "--rng_seed", row_left, 0, "0"); row_left += 1
        self.add_field("Num Workers", "--num_workers", row_left, 0, "0"); row_left += 1
        self.add_checkbox("Use GPU", "--use_gpu", row_left, 0, False); row_left += 1
        self.add_checkbox("H2O Solvents", "--h2o_solvents", row_left, 0, False); row_left += 1
        self.add_checkbox("Verbose", "--verbose", row_left, 0, False); row_left += 1
        self.add_checkbox("Replicate MCTS", "--replicate_mcts", row_left, 0, False); row_left += 1
        self.add_checkbox("Replicate RL", "--replicate_rl", row_left, 0, False); row_left += 1
        
        # --- Column 1 (Scores, RL Settings, Misc) ---
        row_right = 0
        self.add_dropdown("Score Types", "--score_types", row_right, 1, ["qed", "clogp", "random_forest", "chemprop", "wavelength", "sp2_network"], default="qed", required=True); row_right += 1
        self.add_field("Score Model Paths", "--score_model_paths", row_right, 1); row_right += 1
        self.add_dropdown("Score Fingerprint Types", "--score_fingerprint_types", row_right, 1, ["rdkit", "morgan", "None"], default="None"); row_right += 1
        self.add_field("Score Names", "--score_names", row_right, 1); row_right += 1
        self.add_field("Base Score Weights", "--base_score_weights", row_right, 1); row_right += 1
        self.add_field("Score Signs", "--score_signs", row_right, 1); row_right += 1
        self.add_field("Success Thresholds", "--success_thresholds", row_right, 1); row_right += 1
        self.add_dropdown("Wavelength Color", "--wavelength_color", row_right, 1, ["None", "blue", "green", "yellow", "orange"], default="None"); row_right += 1
        
        tk.Frame(self.form_frame, height=2, bd=1, relief=tk.SUNKEN).grid(row=row_right, column=1, sticky="ew", pady=5); row_right += 1

        self.add_dropdown("RL Model Type", "--rl_model_type", row_right, 1, ["chemprop", "mlp"], default="chemprop"); row_right += 1
        self.add_dropdown("RL Model Fingerprint Type", "--rl_model_fingerprint_type", row_right, 1, ["None", "rdkit", "morgan"], default="None"); row_right += 1
        self.add_field("RL Model Paths", "--rl_model_paths", row_right, 1); row_right += 1
        self.add_dropdown("RL Prediction Types", "--rl_prediction_types", row_right, 1, ["classification", "regression"], default="classification"); row_right += 1
        self.add_field("RL Base Temperature", "--rl_base_temperature", row_right, 1, "0.1"); row_right += 1
        self.add_field("RL Temperature Similarity Target", "--rl_temperature_similarity_target", row_right, 1, "0.6"); row_right += 1
        self.add_field("RL Train Frequency", "--rl_train_frequency", row_right, 1, "10"); row_right += 1
        self.add_field("RL Train Epochs", "--rl_train_epochs", row_right, 1, "5"); row_right += 1
        self.add_checkbox("RL Extended Evaluation", "--rl_extended_evaluation", row_right, 1, False); row_right += 1
        self.add_field("Rolling Average Weight", "--rolling_average_weight", row_right, 1, "0.98"); row_right += 1
        self.add_checkbox("No Building Block Diversity", "--no_building_block_diversity", row_right, 1, False); row_right += 1
        self.add_checkbox("Store Nodes", "--store_nodes", row_right, 1, False); row_right += 1
        
        tk.Frame(self.form_frame, height=2, bd=1, relief=tk.SUNKEN).grid(row=row_right, column=1, sticky="ew", pady=5); row_right += 1

        self.add_checkbox("Wandb Log", "--wandb_log", row_right, 1, False); row_right += 1
        self.add_field("Wandb Project Name", "--wandb_project_name", row_right, 1, "synthemol"); row_right += 1
        self.add_field("Wandb Run Name", "--wandb_run_name", row_right, 1); row_right += 1

    def build_run_button(self):
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Generate CLI Command", command=self.show_command, bg="blue", fg="white").pack(side="left", padx=5)
        tk.Button(btn_frame, text="Run Generation", command=self.run_script, bg="green", fg="white").pack(side="left", padx=5)

    def build_output_console(self):
        self.output = scrolledtext.ScrolledText(self.root, height=15)
        self.output.pack(fill="both", expand=False, padx=5, pady=5)

    def get_command(self, include_python=True):
        cmd = []
        if include_python:
            cmd.extend([sys.executable, "synthemol/generate/generate.py"])
        else:
            cmd.append("python synthemol/generate/generate.py")

        missing_required = []
        for key, info in self.entries.items():
            widget = info["widget"]
            required = info["required"]
            label = info["label"]

            if isinstance(widget, (tk.Entry, ttk.Combobox)):
                value = widget.get().strip()
                if value and value != "None":
                    cmd.extend([key, value])
                elif required:
                    missing_required.append(label)
            elif isinstance(widget, tk.BooleanVar):
                if widget.get():
                    cmd.append(key)
        
        if missing_required:
            messagebox.showwarning("Missing Required Fields", f"The following fields are required:\n- {tuple(missing_required)}")
            return None

        return cmd

    def show_command(self):
        cmd = self.get_command(include_python=False)
        if cmd:
            self.output.insert(tk.END, f"CLI Command:\n{' '.join(cmd)}\n\n")
            self.output.see(tk.END)

    def run_script(self):
        cmd = self.get_command(include_python=True)
        if not cmd:
            return

        try:
            self.output.insert(tk.END, f"Running: {' '.join(cmd)}\n\n")

            process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True
            )

            for line in process.stdout:
                self.output.insert(tk.END, line)
                self.output.see(tk.END)
                self.root.update()

            process.wait()

            messagebox.showinfo("Done", "Generation completed!")

        except Exception as e:
            messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = SyntheMolGUI(root)
    root.mainloop()