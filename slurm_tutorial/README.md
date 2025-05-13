# Slurm Tutorial
基本コマンド
```bash
sbatch <script.sh> # ジョブ投入
srun <command> # コマンド実行
scancel <job_id> # 指定ジョブのキャンセル
squeue -u $USER # 自分のジョブ一覧表示
scontrol show job <job_id> # ジョブの詳細情報表示
```
実行・使用状況確認コマンド
```bash
sacct -u $USER # 完了済みジョブも含めた履歴表示
sstat -j <job_id>.batch # 実行中ジョブのCPU/メモリ使用状況
sinfo # パーティションとノードの状態表示
squeue --start -u $USER # 自分のジョブがいつ開始される予定か予測
```
