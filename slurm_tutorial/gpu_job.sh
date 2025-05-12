#!/bin/bash
#SBATCH --job-name=gpu_test              # ジョブ名
#SBATCH --output=job_output.log          # 標準出力・エラー出力ファイル
#SBATCH --partition=gpu                  # GPU用のパーティション名（環境によって異なる）
#SBATCH --gres=gpu:1                     # GPUを1つ要求
#SBATCH --cpus-per-task=4                # CPUスレッド数（任意）
#SBATCH --mem=16G                        # メモリ指定
#SBATCH --time=02:00:00                  # 最大実行時間

# モジュールロード（必要に応じて）
module load cuda/12.2                    # 使用するCUDAバージョン

# Pythonスクリプトの実行（例）
python train_model.py