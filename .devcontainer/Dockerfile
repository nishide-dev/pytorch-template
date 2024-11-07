FROM nvidia/cuda:12.1.1-devel-ubuntu22.04 as builder

WORKDIR /opt

ENV RYE_HOME="/opt/rye"
ENV PATH="$RYE_HOME/shims:$PATH"

# 必要なパッケージのインストール
# hadolint ignore=DL3008
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        ca-certificates \
        curl \
        bash \
        build-essential \
        git \
    && rm -rf /var/lib/apt/lists/*

SHELL [ "/bin/bash", "-o", "pipefail", "-c" ]
RUN curl -sSf https://rye.astral.sh/get | RYE_INSTALL_OPTION="--yes" bash && \
    rye config --set-bool behavior.global-python=true && \
    rye config --set-bool behavior.use-uv=true

COPY ./.python-version ./pyproject.toml ./requirements* README.md ./
RUN rye pin "$(cat .python-version)" && \
    rye sync


FROM nvidia/cuda:12.1.1-devel-ubuntu22.04

# 開発環境用のパッケージインストール
# hadolint ignore=DL3008
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        git \
        openssh-client \
        less \
        iproute2 \
        procps \
        lsb-release \
        locales \
        nvidia-cuda-toolkit \
    && rm -rf /var/lib/apt/lists/*

# ロケールの設定
RUN echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen && \
    locale-gen

# 非rootユーザーの作成
RUN groupadd -g 1000 vscode && \
    useradd -u 1000 -g vscode -s /bin/bash -m vscode

COPY --from=builder /opt/rye /opt/rye

ENV RYE_HOME="/opt/rye"
ENV PATH="$RYE_HOME/shims:$PATH"
ENV PYTHONUNBUFFERED True

RUN rye config --set-bool behavior.global-python=true && \
    rye config --set-bool behavior.use-uv=true

RUN chown -R vscode $RYE_HOME

# GPUサポート用の環境変数
ENV NVIDIA_VISIBLE_DEVICES all
ENV NVIDIA_DRIVER_CAPABILITIES compute,utility,graphics
